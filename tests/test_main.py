import sys
import pytest
from unittest.mock import patch, MagicMock

import main


def test_load_command(monkeypatch, capsys):
    urls = ["https://site.com/news1", "https://site.com/news2"]
    # Mock scrape_news to return predictable data
    monkeypatch.setattr(main, "run_find",
                        lambda url: {'id': 'uuid', 'title': 'Test Title', 'content': 'Content here'})
    # Simulate sys.argv for 'load'
    testargs = ["src/main.py", "load"] + urls
    with patch.object(sys, "argv", testargs):
        main.main()
        out = capsys.readouterr().out
        assert "Scraping news from https://site.com/news1" in out
        assert "Scraping news from https://site.com/news2" in out


def test_find_command(monkeypatch, capsys):
    query = "AI revolution"
    fake_result = {'data': None, 'distances': [[0.12]], 'documents': [['The AI content.']], 'embeddings': None,
                   'ids': [[]],
                   'included': ['documents'], 'metadatas': [[{'title': "AI News"}]], 'uris': None}

    monkeypatch.setattr("main.semantic_search", lambda q, **kwargs: fake_result)
    testargs = ["main.py", "find", query, "--limit", "5"]
    with patch.object(sys, "argv", testargs):
        main.main()
        out = capsys.readouterr().out.title()
        assert "Performing Semantic Search For: 'Ai Revolution'" in out


def test_no_command_shows_help(capsys):
    # Simulate empty command
    testargs = ["main.py"]
    with patch.object(sys, "argv", testargs):
        with pytest.raises(SystemExit):  # Will call sys.exit(1)
            main.main()
        out = capsys.readouterr().out
        assert "usage:" in out
        assert "load" in out
        assert "find" in out
