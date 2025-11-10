"""
Defines the ArticleData class for structured article and embedding storage.
"""
from typing import List, Dict, Optional


class ArticleData:
    """
    Represents article data for storage and embedding.

    Attributes:
        article_id (str): Unique ID for the article/document.
        article_text (str): The raw article text.
        embedding (List[float]): The vector embedding for the article.
        metadata (Dict[str, any]): Metadata about the article (e.g., title, url).
    """

    def __init__(
            self,
            article_id: str,
            article_text: str,
            summary: str,
            embedding: List[float],
            metadata: Optional[Dict[str, any]] = None,
    ):
        self.article_id = article_id
        self.article_text = article_text
        self.summary = summary
        self.embedding = embedding
        self.metadata = metadata if metadata else {}
