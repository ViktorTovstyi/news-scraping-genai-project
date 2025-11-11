import pytest
from unittest.mock import patch, MagicMock

import scraper


# ----------------- scrape_news Tests -----------------

def test_scrape_news_happy_path():
    html = """
    <html><head><title>Sample News</title></head>
    <body>
        <h1>News Headline</h1>
        <article><p>This is the main article paragraph.</p></article>
    </body></html>
    """
    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = html
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp

        title, content = scraper.scrape_news("https://test.com/news")
        assert title == "News Headline"
        assert "main article paragraph" in content

def test_scrape_news_no_article_tag():
    html = "<html><head><title>No Article</title></head>" \
           "<body><p>Hello Paragraph!</p></body></html>"
    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = html
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp

        title, content = scraper.scrape_news("https://test.com/news2")
        assert title == "No Article"
        assert "Hello Paragraph!" in content

def test_scrape_news_no_h1_or_title():
    html = "<html><body><article><p>Just text.</p></article></body></html>"
    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = html
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp

        title, content = scraper.scrape_news("https://test.com/nohead")
        assert title is None
        assert "Just text." in content

def test_scrape_news_request_error():
    with patch("requests.get", side_effect=Exception("404 Error")):
        result = scraper.scrape_news("https://bad.com")
        assert result['title'] is None
        assert result['content'] is None

def test_scrape_news_empty_content():
    html = "<html><head><title>Sample</title></head><body></body></html>"
    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = html
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp

        title, content = scraper.scrape_news("https://test.com/news3")
        assert title == "Sample"
        assert content == ""

# ----------------- scrape_article (integration) -----------------

def test_scrape_article_batch(monkeypatch):
    calls = []
    def fake_scrape_news(url):
        calls.append(url)
        return "title", "content"
    def fake_log(msg): pass
    def fake_summarize_article(text): return "summary"
    def fake_store(data): calls.append("store")

    monkeypatch.setattr(scraper, "scrape_news", fake_scrape_news)
    monkeypatch.setattr(scraper, "log", fake_log)
    monkeypatch.setattr(scraper, "summarize_article", fake_summarize_article)
    monkeypatch.setattr(scraper, "store_data_in_db", fake_store)

    urls = ["https://foo", "https://bar"]
    scraper.scrape_article(urls)
    assert "https://foo" in calls and "https://bar" in calls and "store" in calls
