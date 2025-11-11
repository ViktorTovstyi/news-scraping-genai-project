# Initialize ChromaDB client
import chromadb

from openia import generate_embedding_openai

persist_directory = "./chroma_db"

client = chromadb.PersistentClient()

# Create a collection for news articles
collection = client.get_or_create_collection(name="news_articles")


def store_data_in_db(articles):
    """
    Stores articles, summaries, and topics in the ChromaDB collection.

    Args:
        collection: The ChromaDB collection instance.
        articles: A list of dictionaries, where each dictionary contains:
                  - id: Unique identifier for the article.
                  - text: Full article text.
                  - summary: GenAI-generated summary.
                  - topics: List of topics extracted using GenAI.
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
