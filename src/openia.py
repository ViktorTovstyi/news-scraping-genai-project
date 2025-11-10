import os
from typing import List

import openai

# Optionally load the OpenAI API key from an environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def summarize_article(article_text, max_tokens=128, model="gpt-3.5-turbo"):
    """
    Generate a summary for a news article using OpenAI GPT (chat model).

    Args:
        article_text (str): The article content to summarize.
        max_tokens (int): Max tokens for summary output.
        model (str): OpenAI chat model to use.

    Returns:
        str: A summary of the article, or None on failure.
    """
    if not article_text or not article_text.strip():
        return None
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": f"Summarize the following article in 3-4 sentences.\n\nArticle:\n{article_text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.4,
        )
        summary = completion.choices[0].message['content'].strip()
        return summary
    except Exception as e:
        print(f"OpenAI summarization failed: {e}")
        return None

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

