import pytest
from unittest.mock import patch, MagicMock

import search


def test_semantic_search_happy_path(monkeypatch):
    # Mock embedding generation
    monkeypatch.setattr(search, "generate_embedding_openai", lambda query: [0.1, 0.2, 0.3])
    # Mock collection object and its .query method
    mock_collection = MagicMock()
    expected_results = {'data': None,
                        'distances': None,
                        'documents': [[]],
                        'embeddings': None,
                        'ids': [[]],
                        'included': ['documents', 'metadatas'],
                        'metadatas': [[]],
                        'uris': None}
    mock_collection.query.return_value = expected_results

    # Test the function
    query = "Test AI"
    results = search.semantic_search(query, n_results=2)
    assert results == expected_results


def test_semantic_search_empty_results(monkeypatch):
    monkeypatch.setattr(search, "generate_embedding_openai", lambda query: [0.5, 0.6])
    mock_collection = MagicMock()
    mock_collection.query.return_value = {}

    results = search.semantic_search("No result query", n_results=1)
    assert results == {'data': None,
                       'distances': None,
                       'documents': [[]],
                       'embeddings': None,
                       'ids': [[]],
                       'included': ['documents', 'metadatas'],
                       'metadatas': [[]],
                       'uris': None}


def test_semantic_search_handles_failed_embedding(monkeypatch):
    # Simulate failed embedding (e.g., API returns None)
    monkeypatch.setattr(search, "generate_embedding_openai", lambda query: None)
    mock_collection = MagicMock()

    with pytest.raises(Exception):  # or specify the exception type if known
        search.semantic_search("fail", n_results=1, collection=mock_collection)
