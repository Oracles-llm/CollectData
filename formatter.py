from __future__ import annotations

import json
import os
import re
import sys
import textwrap
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests

BASE_DIR = Path(__file__).resolve().parent
EXTRACTED_TEXT_DIR = BASE_DIR / "ExtractedTextFolder"
OUTPUT_DIR = BASE_DIR / "Outputs"

MODEL_NAME = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

MAX_PARALLEL_REQUESTS = max(2, min(8, (os.cpu_count() or 2) * 2))
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 5
REQUEST_TIMEOUT = 120
MAX_CHAR_PER_REQUEST = 60_000

SYSTEM_INSTRUCTION = (
    "You are an expert educational content curator. Given raw extracted text from "
    "articles or ebooks, identify the core technical knowledge and produce rigorous "
    "question-answer (QA) pairs that could be used in a flashcard dataset. Ignore "
    "headers, navigation menus, author biographies, tables of content, repetitive "
    "page numbers, and any boilerplate. Only rely on facts explicitly present in "
    "the text snippet you receive."
)

PROMPT_TEMPLATE = textwrap.dedent(
    """
    Create a JSON array of rich QA pairs from the provided document. Each array item must
    have exactly two keys: "question" and "answer".

    Guidelines:
    - Write concise but complete questions that target a single concept.
    - Provide precise, self-contained answers grounded in the document.
    - Prefer covering a diverse set of subtopics over repeating similar ideas.
    - Skip speculative content or areas the source text does not explain clearly.
    - Aim for 15-20 QA pairs. If the document is short, produce as many high-quality pairs
      as possible without inventing details.
    - Return JSON only. Do not wrap in Markdown fences or include commentary.

    Source file: {file_name}
    Document excerpt (trimmed to fit the model limits):
    \"\"\"
    {document_text}
    \"\"\"
    """
).strip()


@dataclass
class TaskResult:
    source: Path
    succeeded: bool
    detail: str


def trim_document(text: str) -> str:
    """Ensure the prompt stays within a manageable size for the API."""
    if len(text) <= MAX_CHAR_PER_REQUEST:
        return text
    ellipsis_notice = "\n... [document truncated for prompt budget] ..."
    return text[: MAX_CHAR_PER_REQUEST - len(ellipsis_notice)].rstrip() + ellipsis_notice


def strip_code_fence(candidate: str) -> str:
    candidate = candidate.strip()
    fence_match = re.match(r"```(?:json)?\s*(.*?)\s*```$", candidate, re.DOTALL)
    if fence_match:
        return fence_match.group(1).strip()
    return candidate


def coerce_to_qa_list(model_text: str) -> list[dict[str, str]]:
    cleaned_text = strip_code_fence(model_text)
    if not cleaned_text.startswith("[") or not cleaned_text.rstrip().endswith("]"):
        start = cleaned_text.find("[")
        end = cleaned_text.rfind("]")
        if start != -1 and end != -1 and end > start:
            cleaned_text = cleaned_text[start : end + 1]

    try:
        payload = json.loads(cleaned_text)
    except json.JSONDecodeError as exc:  # pragma: no cover - defensive
        raise ValueError(f"Model output was not valid JSON: {exc}") from exc

    if isinstance(payload, dict):
        payload = [payload]

    if not isinstance(payload, list):
        raise ValueError("Model output must be a JSON array of QA objects.")

    qa_pairs: list[dict[str, str]] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        question = str(item.get("question", "")).strip()
        answer = str(item.get("answer", "")).strip()
        if question and answer:
            qa_pairs.append({"question": question, "answer": answer})

    if not qa_pairs:
        raise ValueError("No valid QA pairs were found in the model response.")

    return qa_pairs


def request_dataset(document_text: str, file_name: str) -> list[dict[str, str]]:
    user_prompt = PROMPT_TEMPLATE.format(
        file_name=file_name,
        document_text=trim_document(document_text),
    )

    payload: dict[str, Any] = {
        "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_prompt}],
            }
        ],
        "generation_config": {
            "temperature": 0.35,
            "top_p": 0.9,
            "top_k": 32,
        },
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(
                API_URL,
                params={"key": GOOGLE_API_KEY},
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            if attempt == MAX_RETRIES:
                raise RuntimeError(f"Request error after {attempt} attempts: {exc}") from exc
            time.sleep(RETRY_BACKOFF_SECONDS * attempt)
            continue

        if response.status_code != 200:
            message = response.text[:500]
            if attempt == MAX_RETRIES:
                raise RuntimeError(
                    f"API responded with status {response.status_code}: {message}"
                )
            time.sleep(RETRY_BACKOFF_SECONDS * attempt)
            continue

        try:
            payload_json = response.json()
        except ValueError as exc:  # pragma: no cover - network safeguard
            raise RuntimeError("API response was not valid JSON.") from exc

        candidates = payload_json.get("candidates") or []
        if not candidates:
            raise RuntimeError("API response did not contain any candidates.")

        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        text_chunks = [part.get("text", "") for part in parts if isinstance(part, dict)]
        model_text = "".join(text_chunks).strip()
        if not model_text:
            raise RuntimeError("API candidate did not contain text.")

        return coerce_to_qa_list(model_text)

    raise RuntimeError("Failed to obtain dataset from API after retries.")  # pragma: no cover


def process_file(path: Path) -> Path:
    document_text = path.read_text(encoding="utf-8", errors="ignore").strip()
    if not document_text:
        raise ValueError("File contained no text to process.")

    qa_pairs = request_dataset(document_text, path.name)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / f"{path.stem}.json"
    destination.write_text(
        json.dumps(qa_pairs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return destination


def gather_text_files() -> list[Path]:
    if not EXTRACTED_TEXT_DIR.exists():
        return []
    files = list(EXTRACTED_TEXT_DIR.glob("*.md"))
    files.extend(EXTRACTED_TEXT_DIR.glob("*.txt"))
    return sorted(files)


def main() -> int:
    if not GOOGLE_API_KEY:
        print("Missing GOOGLE_API_KEY. Set an environment variable or update formatter.py.", file=sys.stderr)
        return 1

    text_files = gather_text_files()
    if not text_files:
        print(f"No markdown or text files found in {EXTRACTED_TEXT_DIR}", file=sys.stderr)
        return 1

    print("=== Stage 2: Generating QA datasets via formatter.py ===")
    print(
        f"Preparing {len(text_files)} file(s). Running up to {MAX_PARALLEL_REQUESTS} concurrent API calls..."
    )

    results: list[TaskResult] = []
    completed = 0

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
        future_map = {executor.submit(process_file, path): path for path in text_files}
        total = len(future_map)
        for future in as_completed(future_map):
            path = future_map[future]
            try:
                output_path = future.result()
            except Exception as exc:
                detail = str(exc)
                results.append(TaskResult(path, False, detail))
                completed += 1
                print(f"[{completed}/{total}] FAIL {path.name} -> {detail}")
                continue

            results.append(TaskResult(path, True, output_path.name))
            completed += 1
            print(f"[{completed}/{total}] OK   {path.name} -> {output_path}")

    failures = [result for result in results if not result.succeeded]
    if failures:
        print("\nThe following files could not be processed:", file=sys.stderr)
        for result in failures:
            print(f"- {result.source.name}: {result.detail}", file=sys.stderr)
        return 1

    print(f"\nStage 2 complete: Saved {len(text_files)} JSON file(s) to {OUTPUT_DIR}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
