"""Batch convert documents inside `Inputs/` to Markdown files in `outputs/` using markitdown."""

import sys
from pathlib import Path

from markitdown import MarkItDown

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "RawInputs"
OUTPUT_DIR = BASE_DIR / "RawOutputs"


def convert_file(converter: MarkItDown, source_path: Path, output_dir: Path) -> None:
    """Convert a single file and write the Markdown result alongside any siblings in output_dir."""

    relative_name = source_path.stem
    destination = output_dir / f"{relative_name}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = converter.convert(str(source_path))
    except Exception as exc:
        print(f"error: failed to convert {source_path.name}: {exc}", file=sys.stderr)
        return

    markdown_text = getattr(result, "text", None)
    if markdown_text is None:
        if isinstance(result, tuple) and result:
            markdown_text = result[0]
        elif isinstance(result, dict) and "text" in result:
            markdown_text = result["text"]
        else:
            markdown_text = str(result)

    destination.write_text(markdown_text, encoding="utf-8")
    print(f"Converted {source_path.name} -> {destination.relative_to(BASE_DIR)}")


def main() -> int:
    if not INPUT_DIR.exists():
        print(f"error: input directory {INPUT_DIR} does not exist", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    converter = MarkItDown()
    files_found = False

    for entry in sorted(INPUT_DIR.iterdir()):
        if entry.is_file():
            files_found = True
            convert_file(converter, entry, OUTPUT_DIR)

    if not files_found:
        print(f"warning: no files found in {INPUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
