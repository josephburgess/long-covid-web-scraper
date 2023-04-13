from flask import jsonify
from src.clients import GuardianClient


def get_news_articles():
    news_client = GuardianClient()
    articles = news_client.search_news("long-covid")
    return jsonify(articles)
