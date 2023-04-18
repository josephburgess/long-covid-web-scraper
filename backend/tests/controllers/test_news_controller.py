import pytest
from unittest.mock import patch
from flask import json
from app import create_app
from .mock_responses import mock_news_articles


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_get_news(client):
    with patch("src.clients.GuardianClient.search_news") as mock_search_news:
        mock_data = mock_news_articles
        mock_search_news.return_value = mock_data

        response = client.get("/api/news")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == len(mock_data)
