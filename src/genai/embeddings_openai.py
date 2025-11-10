"""
OpenAI Embedding Generation Utility.

This module provides a function to generate text embeddings using OpenAI's Embeddings API.
"""
import os
from typing import List

import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_embedding_openai(text, model="text-embedding-ada-002") -> List[float] | None:
    """
    Generates an embedding for the input text using OpenAI's Embeddings API.

    Args:
        text (str): Text to generate the embedding for.
        model (str): OpenAI embedding model name (default: "text-embedding-ada-002").

    Returns:
        list[float] or None: The generated embedding vector, or None on error.
    """
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not found in environment!")
    if not text or not text.strip():
        print("Input text is empty.")
        return None
    try:
        response = openai.Embedding.create(
            input=[text],
            model=model,
        )
        embedding = response['data'][0]['embedding']
        return embedding
    except Exception as e:
        print(f"OpenAI embedding error: {e}")
        return None
