import pytest
from unittest.mock import patch
from flask import json
from app import create_app
from .mock_responses import mock_reddit_posts


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


@patch("src.controllers.reddit_controller.RedditClient")
def test_get_reddit_data(mock_reddit_client, client):
    mock_data = mock_reddit_posts
    mock_reddit_client.return_value.load_posts.return_value = mock_data

    data = {"searchTerms": ["long-covid"]}
    response = client.post("/api/reddit", json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == len(mock_data)
