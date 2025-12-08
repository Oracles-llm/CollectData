from __future__ import annotations

import json
import os
import re
import sys
import textwrap
import threading
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

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyCBtWJErQIyH99yW8_jOTf44d6aPlrj79c")

MAX_PARALLEL_REQUESTS = max(2, min(8, (os.cpu_count() or 2) * 2))
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 5
REQUEST_TIMEOUT = 120
MAX_CHAR_PER_REQUEST = 60_000

# Rate limiting: 10 RPM, but we'll use 9 per batch to be safe
RATE_LIMIT_RPM = 10
RATE_LIMIT_BATCH_SIZE = 9  
RATE_LIMIT_WINDOW_SECONDS = 60

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


class RateLimiter:
    """Thread-safe rate limiter for API requests."""
    
    def __init__(self, batch_size: int = RATE_LIMIT_BATCH_SIZE, window_seconds: int = RATE_LIMIT_WINDOW_SECONDS):
        self.batch_size = batch_size
        self.window_seconds = window_seconds
        self.lock = threading.Lock()
        self.request_count = 0
        self.window_start = time.time()
    
    def wait_if_needed(self) -> None:
        """Wait if we've reached the batch limit, then reset the window."""
        with self.lock:
            current_time = time.time()
            elapsed = current_time - self.window_start
            
            if self.request_count >= self.batch_size:
                wait_time = self.window_seconds - elapsed
                if wait_time > 0:
                    print(f"Rate limit reached ({self.batch_size} requests). Waiting {wait_time:.1f} seconds for quota reset...")
                    time.sleep(wait_time)
                    self.window_start = time.time()
                    self.request_count = 0
                else:
                    self.window_start = current_time
                    self.request_count = 0
            elif elapsed >= self.window_seconds:
                self.window_start = current_time
                self.request_count = 0
            self.request_count += 1

_rate_limiter = RateLimiter()


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
    skipped_items = 0
    for item in payload:
        if not isinstance(item, dict):
            skipped_items += 1
            continue
        question = str(item.get("question", "")).strip()
        answer = str(item.get("answer", "")).strip()
        if question and answer:
            qa_pairs.append({"question": question, "answer": answer})
        else:
            skipped_items += 1

    if not qa_pairs:
        preview = cleaned_text[:200] if len(cleaned_text) > 200 else cleaned_text
        error_msg = (
            f"No valid QA pairs were found in the model response. "
            f"Found {len(payload)} items in payload, but none had valid question/answer pairs. "
            f"Response preview: {preview}..."
        )
        raise ValueError(error_msg)

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
        # Apply rate limiting before making the request
        _rate_limiter.wait_if_needed()
        
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
            error_msg = f"API responded with status {response.status_code}: {message}"
            print(f"WARNING: {error_msg} (attempt {attempt}/{MAX_RETRIES})", file=sys.stderr)
            if attempt == MAX_RETRIES:
                raise RuntimeError(error_msg)
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
        print("ERROR: Missing GOOGLE_API_KEY. Set an environment variable or update formatter.py.", file=sys.stderr)
        print("DEBUG: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
        return 1

    print(f"DEBUG: GOOGLE_API_KEY is set (length: {len(GOOGLE_API_KEY) if GOOGLE_API_KEY else 0})")

    text_files = gather_text_files()
    if not text_files:
        print(f"ERROR: No markdown or text files found in {EXTRACTED_TEXT_DIR}", file=sys.stderr)
        print(f"DEBUG: Directory exists: {EXTRACTED_TEXT_DIR.exists()}", file=sys.stderr)
        if EXTRACTED_TEXT_DIR.exists():
            all_files = list(EXTRACTED_TEXT_DIR.glob("*"))
            print(f"DEBUG: Files in directory: {[f.name for f in all_files]}", file=sys.stderr)
        return 1

    print("=== Stage 2: Generating QA datasets via formatter.py ===")
    print(f"Found {len(text_files)} file(s) to process:")
    for f in text_files:
        print(f"  - {f.name}")
    print(f"Running up to {MAX_PARALLEL_REQUESTS} concurrent API calls...")
    print(f"Rate limit: {RATE_LIMIT_BATCH_SIZE} requests per {RATE_LIMIT_WINDOW_SECONDS} seconds")

    def process_files_batch(files_to_process: list[Path], batch_label: str) -> list[TaskResult]:
        """Process a batch of files and return results."""
        results: list[TaskResult] = []
        completed = 0
        
        with ThreadPoolExecutor(max_workers=MAX_PARALLEL_REQUESTS) as executor:
            future_map = {executor.submit(process_file, path): path for path in files_to_process}
            total = len(future_map)
            for future in as_completed(future_map):
                path = future_map[future]
                try:
                    output_path = future.result()
                except Exception as exc:
                    detail = str(exc)
                    results.append(TaskResult(path, False, detail))
                    completed += 1
                    print(f"[{batch_label}] [{completed}/{total}] FAIL {path.name} -> {detail}")
                    continue

                results.append(TaskResult(path, True, output_path.name))
                completed += 1
                print(f"[{batch_label}] [{completed}/{total}] OK   {path.name} -> {output_path}")
        
        return results

    print("\n--- First Pass: Processing all files ---")
    all_results = process_files_batch(text_files, "PASS 1")
    
    first_pass_failures = [result for result in all_results if not result.succeeded]
    first_pass_successes = [result for result in all_results if result.succeeded]
    
    if first_pass_failures:
        failed_files = [result.source for result in first_pass_failures]
        print(f"\n--- Retry Pass: {len(failed_files)} file(s) failed, waiting 60 seconds before retry ---")
        print("Waiting for rate limit window to reset and retrying failed files...")
        time.sleep(60) 
        
        print(f"\n--- Retrying {len(failed_files)} failed file(s) ---")
        retry_results = process_files_batch(failed_files, "RETRY")
        
        retry_successes = [result for result in retry_results if result.succeeded]
        retry_failures = [result for result in retry_results if not result.succeeded]
        
        all_results = first_pass_successes + retry_successes + retry_failures
        
        if retry_successes:
            print(f"\n✓ Retry successful: {len(retry_successes)} file(s) processed after retry")
        if retry_failures:
            print(f"\n✗ Retry failed: {len(retry_failures)} file(s) still could not be processed")
    
    final_failures = [result for result in all_results if not result.succeeded]
    final_successes = [result for result in all_results if result.succeeded]
    
    if final_failures:
        print(f"\nThe following {len(final_failures)} file(s) could not be processed after retry:", file=sys.stderr)
        for result in final_failures:
            print(f"  - {result.source.name}: {result.detail}", file=sys.stderr)
    
    if final_successes:
        print(f"\nStage 2 complete: Successfully saved {len(final_successes)} JSON file(s) to {OUTPUT_DIR}.")
        if final_failures:
            print(f"Note: {len(final_failures)} file(s) failed after retry, but workflow continues with successful files.")
        return 0
    else:
        print("\nERROR: All files failed to process, even after retry.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
