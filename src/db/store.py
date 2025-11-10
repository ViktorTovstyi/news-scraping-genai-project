# Initialize ChromaDB client
import chromadb
from chromadb import Settings

from src.genai.openia import generate_embedding_openai

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
        title_embedding = generate_embedding_openai(article["title"])
        article_embedding = generate_embedding_openai(article["text"])
        summary_embedding = generate_embedding_openai(article["summary"])
        topic_embedding = generate_embedding_openai(", ".join(article["topics"]))

        # Add to ChromaDB collection
        collection.add(
            documents=[article["title"], article["text"], article["summary"], ", ".join(article["topics"])],
            metadatas=[{"type": "title"}, {"type": "text"}, {"type": "summary"}, {"type": "topics"}],
            ids=[f"{article['id']}_title", f"{article['id']}_text", f"{article['id']}_summary",
                 f"{article['id']}_topics"],
            embeddings=[title_embedding, article_embedding, summary_embedding, topic_embedding],
        )
