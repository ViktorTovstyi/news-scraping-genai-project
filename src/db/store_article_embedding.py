# store_article_embedding.py
"""
Utility to store articles and their embeddings in a ChromaDB collection.
Includes explicit ChromaDB client/collection initialization function, and uses ArticleData class.
"""

import chromadb
from src.db.article_data import ArticleData

def get_chromadb_collection(
    collection_name="news_articles", 
    persist_directory="./data/embeddings"
):
    """
    Initialize and return a ChromaDB client and the requested collection.

    Args:
        collection_name (str): Name of collection for storage/retrieval.
        persist_directory (str): Path to persistent data directory.

    Returns:
        tuple: (client, collection)
    """
    client = chromadb.Client(
        chromadb.config.Settings(persist_directory=persist_directory)
    )
    collection = client.get_or_create_collection(name=collection_name)
    return client, collection

def store_article_embedding(
    article_data: ArticleData,
    collection_name="news_articles", 
    persist_directory="./data/embeddings"
):
    """
    Store an ArticleData object in a ChromaDB collection.

    Args:
        article_data (ArticleData): The article data instance.
        collection_name (str): Name of the ChromaDB collection.
        persist_directory (str): Directory to persist the ChromaDB data.

    Returns:
        None
    """
    client, collection = get_chromadb_collection(
        collection_name=collection_name, 
        persist_directory=persist_directory
    )

    collection.upsert(
        ids=[article_data.article_id],
        embeddings=[article_data.embedding],
        documents=[article_data.article_text],
        metadatas=[article_data.metadata]
    )

# Example usage:
# from src.db.article_data import ArticleData
# article = ArticleData(
#     article_id="12345",
#     article_text="This is an example article.",
#     embedding=[0.1, 0.2, 0.3],
#     metadata={"title": "Sample Article", "url": "https://example.com"}
# )
# store_article_embedding(article)
