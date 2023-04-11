from flask import Blueprint, jsonify, request
from src.clients import RedditClient, GuardianClient
from src.database import get_db
from bson import json_util


bp = Blueprint("routes", __name__)


@bp.route("/api/data")
def get_data():
    db = get_db()
    collection = db.processed_articles
    cursor = collection.find({}).sort("publication_date", -1)
    data_list = list(cursor)
    return json_util.dumps(data_list, default=json_util.default)


@bp.route("/api/news")
def get_news():
    news_client = GuardianClient()
    articles = news_client.search_news("long-covid")
    return jsonify(articles)


@bp.route("/api/reddit", methods=["POST"])
def get_reddit_data():
    search_terms = request.json.get("searchTerms", [])
    reddit_client = RedditClient(search_terms=search_terms)
    posts = reddit_client.load_posts()
    return jsonify(posts)
