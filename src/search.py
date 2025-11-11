"""
search.py

Semantic search functionality for the ChromaDB collection containing news articles.
Provides a function to perform semantic search over stored articles using embeddings.
"""
from store import collection
from openia import generate_embedding_openai

def semantic_search(query, n_results=5):
    """
    Perform semantic search on the ChromaDB collection with a text query.

    Args:
        query (str): The user query to be vectorized and searched.
        n_results (int): The number of top results to return (default: 5).

    Returns:
        dict: Results object containing matched documents and metadata.
    """
    # Generate embedding for the query
    query_embedding = generate_embedding_openai(query)
    # Query the vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas"],
    )
    return results
