# summarizer.py
"""
Integration with OpenAI GPT for article summarization.
"""
import os
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
