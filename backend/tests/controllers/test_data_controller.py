import pytest
from unittest.mock import patch
from flask import json
from app import create_app
from .mock_responses import mock_research_data


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


@patch("src.controllers.data_controller.get_db")
def test_get_data(mock_get_db, client):
    mock_data = mock_research_data
    mock_get_db.return_value.processed_articles.find.return_value.sort.return_value = (
        mock_data
    )

    response = client.get("/api/data")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == len(mock_data)
