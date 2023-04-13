import pytest
from flask import json
from app import create_app


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


def test_get_reddit_data(client):
    data = {"searchTerms": ["long-covid"]}
    response = client.post("/api/reddit", json=data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
