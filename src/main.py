# main.py
# Orchestrates the news scraping, summarization, storage, and semantic search pipeline.
from scraping.scraper import scrape_news
from search.semantic_search import search_articles
from src.db.article_data import ArticleData
from src.db.store_article_embedding import store_article_embedding
from src.genai.embeddings_openai import generate_embedding_openai
from src.genai.summarizer import summarize_article
from utils import log
import uuid


def main():
    url = "https://edition.cnn.com/2025/11/08/europe/ukraine-russia-power-attack-intl"
    log(f"Scraping news from {url}")
    (title, content) = scrape_news(url)

    summary = summarize_article(content)
    log(f"Summarizing article: {summary}")

    embedding = generate_embedding_openai(content)
    log(f"Embedding: {embedding}")

    article_id = str(uuid.uuid4())  # Generate a random unique article ID
    article_data = ArticleData(
        article_id=article_id,
        article_text=content,
        summary=summary,
        embedding=embedding,
        metadata={"title": title, "url": url}
    )

    store_article_embedding(article_data)

    # Example semantic search
    query = "Something about Mars."
    log(f"Semantic search for query: '{query}'")
    search_results = search_articles(query)
    log(f"Search results: {search_results}")

if __name__ == "__main__":
    main()
