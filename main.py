from __future__ import annotations

import shutil
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILTER_SCRIPT = BASE_DIR / "filter.py"
FORMATTER_SCRIPT = BASE_DIR / "formatter.py"
EXTRACTED_TEXT_DIR = BASE_DIR / "ExtractedTextFolder"

# Toggle whether the ExtractedTextFolder should be removed after formatting runs.
# Keep intermediates by default so the data can be inspected or reused.
DELETE_INTERMEDIATE_TEXT = False


def run_script(script_path: Path, label: str) -> None:
    if not script_path.exists():
        raise FileNotFoundError(f"{script_path.name} missing at {script_path}")

    print(f"\n>>> {label} (python {script_path.name})")
    start = time.time()
    subprocess.run([sys.executable, str(script_path)], check=True, cwd=BASE_DIR)
    elapsed = time.time() - start
    print(f"<<< Completed {script_path.name} in {elapsed:.1f}s")


def maybe_cleanup() -> None:
    if not DELETE_INTERMEDIATE_TEXT:
        print("\nPreserving ExtractedTextFolder (set DELETE_INTERMEDIATE_TEXT=True to remove).")
        return

    if not EXTRACTED_TEXT_DIR.exists():
        print("\nExtractedTextFolder already absent; nothing to clean.")
        return

    print("\nDeleting ExtractedTextFolder as requested...")
    shutil.rmtree(EXTRACTED_TEXT_DIR, ignore_errors=True)
    print("ExtractedTextFolder removed.")


def main() -> int:
    try:
        run_script(FILTER_SCRIPT, "Stage 1/2")
        run_script(FORMATTER_SCRIPT, "Stage 2/2")
    except subprocess.CalledProcessError as exc:
        print(f"\nWorkflow halted: {exc}", file=sys.stderr)
        return exc.returncode
    except FileNotFoundError as exc:
        print(f"\n{exc}", file=sys.stderr)
        return 1

    maybe_cleanup()
    print("\nWorkflow finished successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
