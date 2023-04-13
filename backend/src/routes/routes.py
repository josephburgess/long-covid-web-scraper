from flask import Blueprint
from src.controllers import get_reddit_posts, get_news_articles, get_research_data


bp = Blueprint("routes", __name__)


@bp.route("/api/data")
def get_data():
    return get_research_data()


@bp.route("/api/news")
def get_news():
    return get_news_articles()


@bp.route("/api/reddit", methods=["POST"])
def get_reddit():
    return get_reddit_posts()
