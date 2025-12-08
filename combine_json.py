from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from rapidfuzz import fuzz
    RAPIDFUZZ_AVAILABLE = True
except ImportError:
    RAPIDFUZZ_AVAILABLE = False

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "Outputs"


def get_combined_filename() -> Path:
    """Generate a unique timestamped filename for the combined dataset."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_combined.json"
    return OUTPUT_DIR / filename

# Configuration
EXACT_MATCH_THRESHOLD = 1.0  # 100% match
FUZZY_MATCH_THRESHOLD = 0.95  # 95% similarity for fuzzy matching
MIN_QUESTION_LENGTH = 2  # Skip very short questions


def normalize_text(text: str) -> str:
    """Industry-standard text normalization with error handling."""
    try:
        if not isinstance(text, str):
            text = str(text)
        
        text = unicodedata.normalize('NFKD', text)
        
        text = text.lower()
        
        text = re.sub(r'[^\w\s]', '', text)
        
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    except Exception as exc:
        return str(text).lower().strip()


def create_content_hash(question: str, answer: str) -> str:
    """Create a hash for exact duplicate detection (Layer 1)."""
    try:
        normalized_q = normalize_text(question)
        normalized_a = normalize_text(answer)
        content = f"{normalized_q}|||{normalized_a}"
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    except Exception as exc:
        content = f"{str(question)}|||{str(answer)}"
        return hashlib.sha256(content.encode('utf-8', errors='ignore')).hexdigest()


def is_fuzzy_duplicate(
    question: str, 
    answer: str, 
    existing_pairs: list[dict[str, str]]
) -> bool:
    """Check for fuzzy duplicates using string similarity (Layer 2)."""
    if not RAPIDFUZZ_AVAILABLE:
        return False
    
    try:
        normalized_q = normalize_text(question)
        normalized_a = normalize_text(answer)
        
        for existing in existing_pairs:
            try:
                existing_q = normalize_text(existing.get("question", ""))
                existing_a = normalize_text(existing.get("answer", ""))
                
                q_similarity = fuzz.ratio(normalized_q, existing_q) / 100.0
                a_similarity = fuzz.ratio(normalized_a, existing_a) / 100.0
                
                combined_similarity = (q_similarity * 0.7) + (a_similarity * 0.3)
                
                if combined_similarity >= FUZZY_MATCH_THRESHOLD:
                    return True
            except Exception:
                continue
        
        return False
    except Exception:
        return False


def load_json_file(json_file: Path) -> list[dict[str, Any]] | None:
    """Safely load and parse a JSON file."""
    try:
        if not json_file.exists():
            print(f"  ! File does not exist: {json_file.name}", file=sys.stderr)
            return None
        
        if not json_file.is_file():
            print(f"  ! Not a file: {json_file.name}", file=sys.stderr)
            return None
        
        file_size = json_file.stat().st_size
        if file_size > 100 * 1024 * 1024:
            print(f"  ! File too large ({file_size / 1024 / 1024:.1f}MB): {json_file.name}", file=sys.stderr)
            return None
        
        if file_size == 0:
            print(f"  ! Empty file: {json_file.name}", file=sys.stderr)
            return None
        
        content = json_file.read_text(encoding="utf-8")
        if not content.strip():
            print(f"  ! Empty content: {json_file.name}", file=sys.stderr)
            return None
        
        data = json.loads(content)
        
        if isinstance(data, dict):
            return [data]
        elif isinstance(data, list):
            return data
        else:
            print(f"  ! Invalid format (not dict or list): {json_file.name}", file=sys.stderr)
            return None
            
    except json.JSONDecodeError as exc:
        print(f"  ! JSON decode error in {json_file.name}: {exc}", file=sys.stderr)
        return None
    except UnicodeDecodeError as exc:
        print(f"  ! Encoding error in {json_file.name}: {exc}", file=sys.stderr)
        return None
    except PermissionError as exc:
        print(f"  ! Permission denied: {json_file.name}: {exc}", file=sys.stderr)
        return None
    except OSError as exc:
        print(f"  ! I/O error reading {json_file.name}: {exc}", file=sys.stderr)
        return None
    except Exception as exc:
        print(f"  ! Unexpected error reading {json_file.name}: {exc}", file=sys.stderr)
        return None


def validate_qa_pair(qa_pair: dict[str, Any]) -> tuple[str, str] | None:
    """Validate and extract question/answer from a QA pair."""
    try:
        if not isinstance(qa_pair, dict):
            return None
        
        question = qa_pair.get("question")
        answer = qa_pair.get("answer")
        
        if question is None or answer is None:
            return None
        
        question = str(question).strip()
        answer = str(answer).strip()
        
        if not question or not answer:
            return None
        
        return (question, answer)
    except Exception:
        return None


def write_combined_file(qa_pairs: list[dict[str, str]], output_file: Path) -> bool:
    """Safely write the combined JSON file."""
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        json_content = json.dumps(qa_pairs, ensure_ascii=False, indent=2)
        output_file.write_text(json_content, encoding="utf-8")
        
        if not output_file.exists():
            print("  ! Error: Combined file was not created", file=sys.stderr)
            return False
        
        try:
            verify_content = json.loads(output_file.read_text(encoding="utf-8"))
            if len(verify_content) != len(qa_pairs):
                print("  ! Warning: Written file size mismatch", file=sys.stderr)
        except Exception as exc:
            print(f"  ! Error: Written file is not valid JSON: {exc}", file=sys.stderr)
            return False
        
        return True
    except PermissionError as exc:
        print(f"  ! Permission denied writing to {output_file}: {exc}", file=sys.stderr)
        return False
    except OSError as exc:
        print(f"  ! I/O error writing to {output_file}: {exc}", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"  ! Unexpected error writing combined file: {exc}", file=sys.stderr)
        return False


def combine_json_files() -> int:
    """Combine all JSON files in Outputs/ into a single file, removing duplicates."""
    try:
        if not OUTPUT_DIR.exists():
            print(f"Error: Output directory {OUTPUT_DIR} does not exist.", file=sys.stderr)
            return 1

        json_files = sorted(OUTPUT_DIR.glob("*.json"))
        
        json_files = [f for f in json_files if not f.name.endswith("_combined.json")]
        
        if not json_files:
            print(f"Error: No JSON files found in {OUTPUT_DIR}", file=sys.stderr)
            return 1

        print(f"=== Combining {len(json_files)} JSON file(s) ===")
        if RAPIDFUZZ_AVAILABLE:
            print("  Using: Exact matching + Fuzzy matching (rapidfuzz)")
        else:
            print("  Using: Exact matching only (install rapidfuzz for fuzzy matching)")
            print("  Install with: pip install rapidfuzz", file=sys.stderr)
        
        all_qa_pairs: list[dict[str, str]] = []
        seen_hashes: set[str] = set()
        exact_duplicates = 0
        fuzzy_duplicates = 0
        skipped_short = 0
        skipped_invalid = 0
        total_pairs = 0
        files_processed = 0
        files_failed = 0

        for json_file in json_files:
            data = load_json_file(json_file)
            
            if data is None:
                files_failed += 1
                continue
            
            files_processed += 1
            file_exact_dup = 0
            file_fuzzy_dup = 0
            file_valid = 0
            
            for qa_pair in data:
                validated = validate_qa_pair(qa_pair)
                
                if validated is None:
                    skipped_invalid += 1
                    continue
                
                question, answer = validated
                
                if len(question) < MIN_QUESTION_LENGTH:
                    skipped_short += 1
                    continue
                
                total_pairs += 1
                
                try:
                    content_hash = create_content_hash(question, answer)
                    if content_hash in seen_hashes:
                        exact_duplicates += 1
                        file_exact_dup += 1
                        continue
                except Exception as exc:
                    print(f"  ! Error creating hash for pair: {exc}", file=sys.stderr)
                    skipped_invalid += 1
                    continue
                
                try:
                    if is_fuzzy_duplicate(question, answer, all_qa_pairs):
                        fuzzy_duplicates += 1
                        file_fuzzy_dup += 1
                        continue
                except Exception as exc:
                    pass
                
                try:
                    seen_hashes.add(content_hash)
                    all_qa_pairs.append({
                        "question": question,
                        "answer": answer
                    })
                    file_valid += 1
                except Exception as exc:
                    print(f"  ! Error adding QA pair: {exc}", file=sys.stderr)
                    skipped_invalid += 1
                    continue
            
            dup_count = file_exact_dup + file_fuzzy_dup
            if dup_count > 0:
                print(f"  ✓ {json_file.name}: {file_valid} unique, {dup_count} duplicate(s)")
            else:
                print(f"  ✓ {json_file.name}: {file_valid} unique")

        if files_failed > 0:
            print(f"\n  ! Warning: {files_failed} file(s) failed to process", file=sys.stderr)

        if not all_qa_pairs:
            print("Error: No valid QA pairs found to combine.", file=sys.stderr)
            return 1

        combined_output_file = get_combined_filename()
        
        if not write_combined_file(all_qa_pairs, combined_output_file):
            print("Error: Failed to write combined file.", file=sys.stderr)
            return 1

        print(f"\n✓ Deduplication Summary:")
        print(f"  Files processed: {files_processed}/{len(json_files)}")
        print(f"  Total QA pairs processed: {total_pairs}")
        print(f"  Unique QA pairs: {len(all_qa_pairs)}")
        print(f"  Exact duplicates removed: {exact_duplicates}")
        if RAPIDFUZZ_AVAILABLE:
            print(f"  Fuzzy duplicates removed: {fuzzy_duplicates}")
        print(f"  Short questions skipped: {skipped_short}")
        print(f"  Invalid pairs skipped: {skipped_invalid}")
        if total_pairs > 0:
            dup_rate = ((exact_duplicates + fuzzy_duplicates) / total_pairs * 100)
            print(f"  Deduplication rate: {dup_rate:.1f}%")
        print(f"  Saved to: {combined_output_file}")
        return 0
        
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"\nFatal error: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(combine_json_files())

