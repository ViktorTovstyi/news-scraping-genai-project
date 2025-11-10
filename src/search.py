from store import collection
from openia import generate_embedding_openai


def semantic_search(query, n_results=5):
    """
    Perform semantic search on the ChromaDB collection.

    Args:
        query: The user query as a string.
        collection: The ChromaDB collection instance.
        n_results: The number of top results to return.

    Returns:
        A list of results containing the most similar documents and metadata.
    """
    # Generate embedding for the query
    query_embedding = generate_embedding_openai(query)

    # Query the vector database
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents"],
    )
    return results
