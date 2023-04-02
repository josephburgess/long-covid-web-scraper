from bson import json_util
from flask import Flask, jsonify
from .clients import RedditClient
from .db_connector import get_db


app = Flask(__name__, static_folder='static')


@app.route("/api/data")
def get_data():
    db = get_db()
    collection = db.processed_articles
    cursor = collection.find({})
    data_list = list(cursor)
    return json_util.dumps(data_list)


@app.route("/api/reddit")
def get_reddit_data():
    reddit_client = RedditClient()
    posts = reddit_client.load_posts()
    return jsonify(posts)


if __name__ == "__main__":
    app.run(debug=True)
