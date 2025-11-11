import pytest
from unittest.mock import patch, MagicMock
import src.openia as openia

def test_summarize_article_success():
    article_text = "This is a long article about AI and technology advances."
    fake_response = MagicMock()
    fake_response.choices = [MagicMock()]
    fake_response.choices[0].message = {'content': 'This is a summary.'}
    with patch.object(openia.openai.ChatCompletion, "create", return_value=fake_response) as mock_create:
        summary = openia.summarize_article(article_text)
        assert summary == "This is a summary."
        mock_create.assert_called_once()

def test_summarize_article_empty():
    assert openia.summarize_article('') is None
    assert openia.summarize_article('   ') is None

def test_summarize_article_api_error():
    article_text = "This is an article."
    with patch.object(openia.openai.ChatCompletion, "create", side_effect=Exception("API error")):
        summary = openia.summarize_article(article_text)
        assert summary is None

def test_generate_embedding_openai_success():
    fake_embedding = [0.1, 0.2, 0.3]
    fake_response = {'data': [{'embedding': fake_embedding}]}
    with patch.object(openia.openai.Embedding, "create", return_value=fake_response) as mock_embed:
        result = openia.generate_embedding_openai("text for embedding")
        assert result == fake_embedding
        mock_embed.assert_called_once()

def test_generate_embedding_openai_empty_text():
    assert openia.generate_embedding_openai("") is None
    assert openia.generate_embedding_openai("   ") is None

def test_generate_embedding_openai_no_api_key(monkeypatch):
    monkeypatch.setattr(openia, "OPENAI_API_KEY", None)
    with pytest.raises(RuntimeError):
        openia.generate_embedding_openai("any text")

def test_generate_embedding_openai_api_error():
    with patch.object(openia.openai.Embedding, "create", side_effect=Exception("API Error!")):
        result = openia.generate_embedding_openai("embed this text")
        assert result is None