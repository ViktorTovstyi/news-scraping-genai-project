# News Scraping, Summarization, and Semantic Search

This project provides powerful tools to extract news articles from URLs, summarize content using GenAI, store semantic vectors, and perform contextual search. It demonstrates the integration of AI, web scraping, and vector databases for real-world applications.

## Features

1. **Article Loader (Scraper)**
   - Fetches full-text articles and headlines from user-provided web URLs via CLI.
2. **GenAI Summarization & Topic Identification**
   - Summarizes articles and identifies main topics using Generative AI (e.g., OpenAI GPT).
3. **Semantic Search (Find)**
   - Enables semantic search: query with a phrase and retrieve relevant articles using vector similarity in ChromaDB.

## Tech Stack

- **Language:** Python
- **Web Scraping:** requests, beautifulsoup4
- **GenAI:** openai
- **Vector DB:** chromadb
- **Embeddings:** sentence-transformers
- **Config/Test:** python-dotenv, pytest
- **Utilities:** numpy, pandas, tqdm

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/news-scraping-genai-project.git
   cd news-scraping-genai-project
   ```

2. **Set Up Virtual Environments:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```
3. **Install Requirements:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Environment Variables:**
   Create a `.env` file in the root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   # (ChromaDB uses local storage by default)
   ```

## Usage

### CLI Commands
- **Load articles from URLs:**
  ```sh
  python src/main.py load "https://news-site.com/article1" "https://news-site.com/article2"
  ```

- **Semantic search over articles:**
  ```sh
  python src/main.py find "machine learning breakthroughs"
  ```
  (Top-K results include similarity score, metadata, and article ID.)

### Input
- Any list of article URLs (for loading/scraping)
- Natural language queries (for searching)

### Output
- Summaries, topics, article vectors, and search results with relevance scores

## Project Structure

```plaintext
news-scraping-genai-project/
│
├── src/
│   ├── main.py                 # CLI loader & semantic search
│   ├── scraper.py              # Scrape articles from URLs
│   ├── summarizer.py           # Summarize article content via GenAI
│   ├── store_article_embedding.py # Store articles+embeddings in ChromaDB
│   ├── semantic_search.py      # Semantic query logic for articles
│   ├── ... other modules
│   └── __init__.py
├── tests/
├── requirements.txt
├── .env
└── docs/
    ├── project-structure.md
    └── dev-notes.md
```

## How It Works

1. **Load:** Use the CLI to load one or more article URLs. Each receives a unique ID. Text is scraped, summarized if configured, and stored with vector embedding.
2. **Find:** Use natural language queries with the CLI to find relevant articles by semantic similarity (vector distance in ChromaDB).

## Testing

Run all tests (if available):
```sh
pytest tests/
```

## Future Enhancements
- Visual interface for search and load
- Additional AI models and vector databases
- Live newsfeeds/RSS ingestion

## Contributing
Open issues or submit pull requests. Please use feature branches and ensure PEP8 compliance.

## License
MIT License

## Contact
- Viktor Tovstyi
- Email: Viktor_Tovstyi@epam.com
- GitHub: https://github.com/ViktorTovstyi/news-scraping-genai-project.git
