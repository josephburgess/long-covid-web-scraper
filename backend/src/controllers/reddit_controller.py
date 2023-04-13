from flask import request, jsonify
from src.clients import RedditClient


def get_reddit_posts():
    search_terms = request.json.get("searchTerms", [])
    reddit_client = RedditClient(search_terms=search_terms)
    posts = reddit_client.load_posts()
    return jsonify(posts)
