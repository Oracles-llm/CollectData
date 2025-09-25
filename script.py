#!/usr/bin/env python3
"""Convert documents into Markdown using markitdown.

Set `SOURCE_FILE` (and optionally `OUTPUT_FILE`) below instead of passing command-line arguments.
"""

import sys
from pathlib import Path
from typing import Optional, Union

from markitdown import MarkItDown

# Base directory used to resolve relative paths for input/output.
BASE_DIR = Path(__file__).resolve().parent

# Update these paths to point to the file you want to convert and where to place the Markdown output.
# Relative paths are resolved from `BASE_DIR` defined above.
SOURCE_FILE: Union[str, Path] = "test.pdf"
OUTPUT_FILE: Optional[Union[str, Path]] = None  # e.g. "converted/test1.md" or Path("out.md")


def resolve_path(path_value: Union[str, Path]) -> Path:
    """Resolve a string or Path relative to BASE_DIR."""
    candidate = Path(path_value)
    if not candidate.is_absolute():
        candidate = BASE_DIR / candidate
    return candidate.resolve()


def resolve_optional_path(path_value: Optional[Union[str, Path]]) -> Optional[Path]:
    if path_value is None:
        return None
    return resolve_path(path_value)


def determine_output_path(source: Path, output_override: Optional[Path]) -> Path:
    if output_override:
        candidate = output_override
        if candidate.exists() and candidate.is_dir():
            return candidate / f"{source.stem}.md"
        if candidate.suffix.lower() != ".md":
            return candidate.with_suffix(".md")
        return candidate
    return source.with_suffix(".md")


def main() -> int:
    source_path = resolve_path(SOURCE_FILE)

    if not source_path.exists():
        print(f"error: {source_path} does not exist", file=sys.stderr)
        return 1

    output_override = resolve_optional_path(OUTPUT_FILE)
    output_path = determine_output_path(source_path, output_override)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    converter = MarkItDown()
    try:
        result = converter.convert(str(source_path))
    except Exception as exc:  # markitdown can raise a variety of errors for unsupported types
        print(f"error: failed to convert {source_path.name}: {exc}", file=sys.stderr)
        return 1

    markdown_text = getattr(result, "text", None)
    if markdown_text is None:
        if isinstance(result, tuple) and result:
            markdown_text = result[0]
        elif isinstance(result, dict) and "text" in result:
            markdown_text = result["text"]
        else:
            markdown_text = str(result)

    output_path.write_text(markdown_text, encoding="utf-8")
    print(f"Converted {source_path.name} -> {output_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
