"""
store.py

Persistent storage utility for news articles in ChromaDB.
Initializes a collection and provides a function to add articles with text,
summary, topics, URL, and embeddings.
"""
import chromadb
from openia import generate_embedding_openai

persist_directory = "./chroma_db"

client = chromadb.PersistentClient()

# Create a collection for news articles
collection = client.get_or_create_collection(name="news_articles")

def store_data_in_db(articles):
    """
    Store a list of articles with associated summaries, topics, and embeddings
    in the ChromaDB collection.

    Args:
        articles (list[dict]): Each dictionary should contain:
            - id (str): Unique identifier.
            - text (str): Full article text.
            - summary (str): GenAI-generated summary.
            - topics (list[str]): Topics extracted with GenAI.
            - url (str): Source URL for the article.

    Returns:
        None
    """
    for article in articles:
        # Generate embeddings
        article_embedding = generate_embedding_openai(article["text"])
        topics = ",".join(article["topics"])
        # Add to ChromaDB collection
        collection.add(
            documents=[article["text"]],
            metadatas=[{"summary": article["summary"], "url": article["url"], "topics": topics}],
            ids=[article['id']],
            embeddings=[article_embedding],
        )
