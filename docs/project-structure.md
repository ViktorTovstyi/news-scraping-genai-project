# Project Structure

```plaintext
news-scraping-genai-project/
│
├── .git/                   # Git repo data
├── .gitignore              # Git ignore file
├── .idea/                  # JetBrains/PyCharm config (if present)
├── .venv/                  # Python virtual environment (if used)
├── chroma/                 # ChromaDB persistent store (if present)
│
├── docs/                   # Project documentation
│   ├── dev-notes.md
│   ├── estimation.md
│   └── project-structure.md
│
├── README.md               # Project main documentation
├── requirements.txt        # Dependencies
│
└── src/                    # Source code directory
    ├── __init__.py         # Makes src a Python package
    ├── main.py             # Main entry point, CLI parser
    ├── openia.py           # OpenAI integration (typo? Should be openai.py)
    ├── scraper.py          # Scrape news articles
    ├── search.py           # Semantic search entry/aggregation
    ├── store.py            # Embedding/document persistence
    ├── utils.py            # Utility functions
    └── __pycache__/        # Python bytecode cache

```

## Current Directory and File Descriptions

- **src/main.py**        – CLI parser. Run article loading or semantic search from the command line.
- **src/scraper.py**     – Scrapes headline and main text from a given news URL, returns a dict.
- **src/search.py**      – Core logic for semantic search/find over your articles (ChromaDB-based).
- **src/store.py**       – Logic for storing article embeddings/documents in ChromaDB.
- **src/utils.py**       – Utilities: logging, error handling, helper functions.
- **src/openia.py**      – OpenAI integrations (may be a typo, consider renaming to openai.py).
- **src/__init__.py**    – Marks the directory as a package.

## Removed/Legacy Folders

- The previous modular dirs `src/scraping/`, `src/genai/`, `src/db/`, `src/search/` do NOT exist in the current structure. All functional code now resides flat in `src/`.
- No `tests/` or `data/` folders are currently present.

## Example Usage

- Run CLI load (scrape and store articles):
  ```bash
  python src/main.py load "https://example.com/news/12345" "https://somewhere.com/news/2"
  ```
- Run CLI find (semantic search):
  ```bash
  python src/main.py find "AI news breakthroughs" --top_k 3
  ```
