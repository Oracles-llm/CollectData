from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import trafilatura

try:
    from PyPDF2 import PdfReader  # type: ignore[import-not-found]
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    PdfReader = None  # type: ignore[assignment]

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "inputs.txt"
LOCAL_INPUT_DIR = BASE_DIR / "Inputs"
RAW_DATA_DIR = BASE_DIR / "RawData"

def sanitize_for_filename(url: str) -> str:
    """Create a filesystem-safe stem from the given URL."""
    parsed = urlparse(url)
    candidate = f"{parsed.netloc}{parsed.path}"
    candidate = candidate or "download"
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", candidate).strip("_")
    return cleaned or "download"

def read_urls(path: Path) -> list[str]:
    if not path.exists():
        print(f"Missing input file: {path}", file=sys.stderr)
        return []
    content = path.read_text(encoding="utf-8")
    return [line.strip() for line in content.splitlines() if line.strip()]

def collect_local_inputs(directory: Path) -> list[Path]:
    if not directory.exists():
        print(f"Missing Inputs folder: {directory}", file=sys.stderr)
        return []
    return sorted([path for path in directory.iterdir() if path.is_file()])

def extract_text_from_html(html: str, *, url: str | None = None) -> str | None:
    return trafilatura.extract(
        html,
        url=url,
        output_format="txt",
        include_comments=False,
        include_formatting=False,
        include_tables=True,
        include_links=False,
        include_images=False,
    )

def extract_text_from_pdf(path: Path) -> str:
    if PdfReader is None:
        raise RuntimeError(
            "PyPDF2 is required to extract text from PDF files. Install it with 'pip install PyPDF2'."
        )
    reader = PdfReader(str(path))
    text_chunks: list[str] = []
    for page in reader.pages:
        text = page.extract_text() or ""
        text_chunks.append(text)
    return "\n".join(text_chunks).strip()

def extract_text_from_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        html = path.read_text(encoding="utf-8", errors="ignore")
        extracted = extract_text_from_html(html)
        if extracted:
            return extracted
        return html
    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".pdf":
        return extract_text_from_pdf(path)
    return path.read_text(encoding="utf-8", errors="ignore")

def write_text_output(stem: str, text: str) -> None:
    destination = RAW_DATA_DIR / f"{stem}.txt"
    destination.write_text(text, encoding="utf-8")

def main() -> None:
    urls = read_urls(INPUT_FILE)
    local_files = collect_local_inputs(LOCAL_INPUT_DIR)

    tasks: list[tuple[str, str | Path]] = []
    tasks.extend(("url", url) for url in urls)
    tasks.extend(("file", path) for path in local_files)

    if not tasks:
        print("No inputs found in inputs.txt or Inputs folder.", file=sys.stderr)
        return

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    total = len(tasks)
    for index, (task_type, payload) in enumerate(tasks, start=1):
        if task_type == "url":
            url = str(payload)
            print(f"[{index}/{total}] Downloading {url}")
            try:
                downloaded_html = trafilatura.fetch_url(url)
            except Exception as exc:
                print(f"  ! Failed to fetch: {exc}", file=sys.stderr)
                continue

            if not downloaded_html:
                print("  ! No HTML retrieved.", file=sys.stderr)
                continue

            extracted_text = extract_text_from_html(downloaded_html, url=url)
            if not extracted_text:
                print(
                    "  ! Failed to extract clean article content. Storing fallback text.",
                    file=sys.stderr,
                )
                extracted_text = (
                    f"Extraction failed. The downloaded HTML for {url} could not be parsed."
                )

            stem = f"{index:03d}_{sanitize_for_filename(url)}"
            write_text_output(stem, extracted_text)
        else:
            path = Path(payload)
            print(f"[{index}/{total}] Reading local file {path.name}")
            try:
                extracted_text = extract_text_from_file(path)
            except Exception as exc:
                print(f"  ! Failed to process {path.name}: {exc}", file=sys.stderr)
                continue

            if not extracted_text:
                print("  ! No text extracted. Skipping file.", file=sys.stderr)
                continue

            stem = f"{index:03d}_{sanitize_for_filename(path.stem)}"
            write_text_output(stem, extracted_text)

    print("Processing complete.")


if __name__ == "__main__":
    main()
