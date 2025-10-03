from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import trafilatura

from services.supabase import supabase_service

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "../inputs.txt"
RAW_DIR = BASE_DIR / "../data/rawInputs/singleton"
OUTPUT_DIR = BASE_DIR / "../data/markdowns/singleton"
CREATOR_NAME = "Neranjan"
DESIGN_PATTERN_NAME = "Singleton"


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


def convert_urls_to_markdown() -> None:
    urls = read_urls(INPUT_FILE)
    if not urls:
        print("No URLs to process.", file=sys.stderr)
        return

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for index, url in enumerate(urls, start=1):
        print(f"[{index}/{len(urls)}] Downloading {url}")
        try:
            downloaded_html = trafilatura.fetch_url(url)
        except Exception as exc:
            print(f"  ! Failed to fetch: {exc}", file=sys.stderr)
            continue

        if not downloaded_html:
            print("  ! No HTML retrieved.", file=sys.stderr)
            continue

        stem = f"{index:03d}_{sanitize_for_filename(url)}"
        raw_path = RAW_DIR / f"{stem}.html"
        raw_path.write_text(downloaded_html, encoding="utf-8")

        markdown_content = trafilatura.extract(
            downloaded_html,
            url=url,
            output_format="markdown",
            include_comments=False,
            include_formatting=True,
            include_tables=True,
            include_links=False,
            include_images=False,
        )

        if not markdown_content:
            print("  ! Failed to extract clean article content.", file=sys.stderr)
            markdown_content = (
                f"# Extraction failed\n\n"
                f"Trafilatura could not extract the main article content from {url}."
            )

        output_path = OUTPUT_DIR / f"{stem}.md"
        output_path.write_text(markdown_content, encoding="utf-8")

        # Save resource details to Supabase
        md_filename = f"{stem}.md"
        try:
            supabase_service.add_resource(
                "resources",
                {
                    "resource_url": url,
                    "md_file_name": md_filename,
                    "date": datetime.now().isoformat(),
                    "design_pattern_name": DESIGN_PATTERN_NAME,
                    "creator_name": CREATOR_NAME,
                },
            )
            print(f"  ✓ Saved to Supabase: {DESIGN_PATTERN_NAME}")
        except Exception as e:
            print(f"  ! Failed to save to Supabase: {e}", file=sys.stderr)

    print("Processing complete.")
