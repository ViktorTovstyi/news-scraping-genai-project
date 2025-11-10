# parser.py
"""
HTML/article parsing utilities.
Parses raw HTML to extract title and article content (for input from 'scrape_news').
"""

from bs4 import BeautifulSoup

def parse_article(html):
    """
    Parse raw HTML content to extract article headline and main text.

    Args:
        html (str): Raw HTML to parse (entire page, not just snippet).

    Returns:
        dict: {
            'title': <headline as str or None>,
            'content': <main article text as str or None>
        }
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Try to extract title, prefer <h1>
    title = None
    h1 = soup.find('h1')
    if h1 and h1.text.strip():
        title = h1.text.strip()
    elif soup.title:
        title = soup.title.string.strip()

    # Try to extract article content from <article>
    article_tag = soup.find('article')
    content = None

    if article_tag:
        content = ' '.join([p.get_text(separator=' ', strip=True) for p in article_tag.find_all('p')])
    else:
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text(separator=' ', strip=True) for p in paragraphs])

    # Clean up whitespace
    if content:
        content = ' '.join(content.split())

    return {'title': title, 'content': content}
