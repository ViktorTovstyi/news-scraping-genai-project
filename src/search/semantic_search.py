# semantic_search.py
"""
Semantic search utility for news articles stored in ChromaDB.
"""

import os
from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# Try to import your OpenAI embedding function if available
try:
    from genai.embeddings_openai import generate_embedding_openai

    EMBEDDING_PROVIDER = "openai"
except ImportError:
    EMBEDDING_PROVIDER = "chromadb"


def create_query_embedding(query_text: str, provider: str = "chromadb"):
    """
    Generate an embedding vector for the search query.
    By default uses OpenAI, with fallback to ChromaDB's sentence transformer.
    """
    if provider == "openai":
        try:
            return generate_embedding_openai(query_text)
        except Exception as e:
            print(f"OpenAI embedding failed, using ChromaDB: {e}")
            provider = "chromadb"
    if provider == "chromadb":
        st_fn = embedding_functions.SentenceTransformerEmbeddingFunction()
        return st_fn([query_text])[0]
    return None


def search_articles(
        query: str,
        collection_name: str = "news_articles",
        persist_directory: str = "./data/embeddings",
        top_k: int = 5,
        embedding_provider: str = EMBEDDING_PROVIDER
):
    """
    Perform semantic search against the articles collection.

    Args:
        query (str): The semantic query string.
        collection_name (str): ChromaDB collection name.
        persist_directory (str): Path to persistent ChromaDB storage.
        top_k (int): Number of results to retrieve.
        embedding_provider (str): "openai" or "chromadb"

    Returns:
        list[dict]: List of results with 'id', 'document', and 'metadata'.
    """
    # Generate embedding for the query
    embedding = create_query_embedding(query, provider=embedding_provider)
    if embedding is None:
        print("Embedding for query could not be generated!")
        return []

    client = Client(Settings(persist_directory=persist_directory))
    collection = client.get_or_create_collection(
        name=collection_name)

    results = collection.query(
        query_texts=[query],
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents", "metadatas"]
    )

    # Format results: list of dicts
    formatted = []
    ids = results.get("ids", [[]])[0]
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]

    for i in range(len(ids)):
        formatted.append({
            "id": ids[i],
            "document": docs[i],
            "metadata": metas[i]
        })
    return formatted

# Example usage:
# results = search_articles("Latest trends in AI technology")
# for res in results:
#     print(f"{res['id']}: {res['metadata'].get('title')} ({res['distance']:.4f})")
