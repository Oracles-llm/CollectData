## Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   If you are installing manually, make sure at least `trafilatura`, `PyPDF2`, and `requests` are present.
3. Provide your Gemini API key. Either export `GOOGLE_API_KEY` in your shell or edit `formatter.py` with the key (an example placeholder is already included).

## Workflow Overview

The pipeline has two stages:

1. `filter.py` reads URLs from `inputs.txt` and local files in the `Inputs/` directory, normalizes their content, and writes cleaned text files to `ExtractedTextFolder/`.
2. `formatter.py` sends each extracted text file to Gemini and stores the generated question/answer dataset as `<stem>.json` in `Outputs/`.

Running the scripts separately is still possible (e.g., `python filter.py`), but most workflows should go through `main.py`.

## Running Everything at Once

```
python main.py
```

`main.py` will:

1. Run `filter.py` (Stage 1) and print detailed progress as it gathers and cleans the sources.
2. Run `formatter.py` (Stage 2) to generate the QA datasets concurrently, reporting success/failure for each file.
3. Optionally delete the `ExtractedTextFolder/` intermediate output. Toggle this behavior by editing the `DELETE_INTERMEDIATE_TEXT` flag at the top of `main.py` (defaults to preserving the folder so you can inspect the raw text).

If any script fails, `main.py` stops immediately and surfaces the error so you can fix the inputs or configuration before retrying.

## Inputs and Outputs

- `inputs.txt`: each non-empty line is treated as a URL to download and extract.
- `Inputs/`: drop local files (HTML, PDF, Markdown, TXT) here to process them alongside the URLs.
- `ExtractedTextFolder/`: generated text files after Stage 1. May be automatically removed, depending on the flag mentioned above.
- `Outputs/`: final JSON datasets. Each file contains an array of `{ "question": ..., "answer": ... }` objects suitable for downstream training or flashcard applications.

## Troubleshooting

- If `filter.py` logs a missing dependency for PDFs, install `PyPDF2`.
- If `formatter.py` reports an authentication error, double-check your `GOOGLE_API_KEY`.
- For large batches, watch the console progress (e.g., `[12/40] OK ...`) to estimate remaining work. The script retries transient API issues automatically, but persistent failures will end up in the summary.
