from flask import json
from app import create_app

app = create_app()


def test_get_data():
    with app.test_client() as client:
        response = client.get("/api/data")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) > 0


def test_get_news():
    with app.test_client() as client:
        response = client.get("/api/news")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) > 0


def test_get_reddit_data():
    with app.test_client() as client:
        data = {"searchTerms": ["long-covid"]}
        response = client.post("/api/reddit", json=data)
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) > 0
