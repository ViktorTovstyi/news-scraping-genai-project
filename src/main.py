# main.py
# Orchestrates the news scraping, summarization, storage, and semantic search pipeline.
from pydoc_data.topics import topics

from scraping.scraper import scrape_news
from src.db.search import semantic_search
from src.db.store import store_data_in_db
from src.genai.openia import summarize_article, generate_embedding_openai
from utils import log


def main():
    url = "https://edition.cnn.com/2025/11/08/europe/ukraine-russia-power-attack-intl"
    log(f"Scraping news from {url}")
    (title, content) = scrape_news(url)

    summary = summarize_article(content)
    log(f"Summarizing article: {summary}")

    store_data_in_db([{"id": "0000", "title": title, "text": content, "summary": summary, "topics": ["News"]}])

    # Example semantic search
    # query = "Something about Mars."
    query = "Mars"
    log(f"Semantic search for query: '{query}'")
    search_results = semantic_search(query)
    log(f"Search results: {search_results}")


if __name__ == "__main__":
    main()
