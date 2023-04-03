from bson import json_util
from flask import Flask, jsonify
from src.clients import RedditClient, GuardianClient
from src.db_connector import get_db
import os


app = Flask(__name__)


@app.route("/api/data")
def get_data():
    db = get_db()
    collection = db.processed_articles
    cursor = collection.find({})
    data_list = list(cursor)
    return json_util.dumps(data_list)


@app.route("/api/news")
def get_news():
    news_client = GuardianClient()
    articles = news_client.search_news('long-covid')
    return jsonify(articles)


@app.route("/api/reddit")
def get_reddit_data():
    reddit_client = RedditClient()
    posts = reddit_client.load_posts()
    return jsonify(posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
