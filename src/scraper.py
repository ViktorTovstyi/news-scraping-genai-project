"""
scraper.py

News scraping utility functions for extracting headlines, main content,
summary, and topics from news articles. Scrapes data from URLs and stores it in the DB.
"""
import uuid
from typing import Any

import requests
from bs4 import BeautifulSoup

from openia import summarize_article
from store import store_data_in_db
from utils import log
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def scrape_news(url):
    """
    Scrape the title and main content from a news article at the given URL.

    Args:
        url (str): The web address to scrape.

    Returns:
        tuple: (title, content), both strings or None on failure.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return (None, None)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Try to extract the title (news sites often use <h1>)
    title = None
    h1 = soup.find('h1')
    if h1 and h1.text.strip():
        title = h1.text.strip()
    elif soup.title:
        title = soup.title.string.strip()

    # Try to extract article text (many sites use <article> tag, fallback to paragraphs)
    article_tag = soup.find('article')
    content = None
    if article_tag:
        content = '\n'.join([p.get_text(separator=' ', strip=True) for p in article_tag.find_all('p')])
    else:
        # Fallback: get all paragraph texts on the page
        paragraphs = soup.find_all('p')
        content = '\n'.join([p.get_text(separator=' ', strip=True) for p in paragraphs])

    # Clean up excessive whitespace
    if content:
        content = '\n'.join(content.split('\n'))

    return title, content

def scrape_article(urls):
    """
    Scrapes and processes a list of article URLs. Extracts headline, content,
    summary, and topics, and stores the results in the database.

    Args:
        urls (list[str]): List of article URLs to scrape.

    Returns:
        None
    """
    for url in urls:
        log(f"Scraping news from {url}")
        (title, content) = scrape_news(url)
        summary = summarize_article(content)
        log(f"Summarizing article: {summary}")
        topics = get_topics(content)
        article_id = str(uuid.uuid4())
        data = {"id": article_id, "title": title, "text": content, "summary": summary, "topics": topics, "url": url}
        log(f"Topics: {topics}")
        store_data_in_db([data])

def get_topics(content) -> list[str]:
    """
    Extracts top topics from an article using zero-shot classification.

    Args:
        content (str): The article text.

    Returns:
        list[str]: List of predicted topics (labels).
    """
    candidate_labels = ["Artificial Intelligence", "Business", "Technology", "Politics", "Environment"]
    result = classifier(content, candidate_labels)
    topics = result['labels'][:4]
    return topics
