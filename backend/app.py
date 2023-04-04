from auth0.authentication import GetToken
from bson import json_util
from flask import Flask, jsonify, request
from src.clients import RedditClient, GuardianClient
from src.db_connector import get_db
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)
load_dotenv()

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ALGORITHM"] = os.getenv("JWT_ALGORITHM")
app.config["JWT_PUBLIC_KEY"] = os.getenv("JWT_PUBLIC_KEY")

jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    token = request.headers.get("Authorization").split(" ")[1]

    domain = os.getenv("AUTH0_DOMAIN")
    audience = os.getenv("AUTH0_AUDIENCE")
    client_id = os.getenv("AUTH0_CLIENT_ID")
    client_secret = os.getenv("AUTH0_CLIENT_SECRET")
    auth0_client = GetToken(domain)
    token_info = auth0_client.login(
        client_id=client_id,
        client_secret=client_secret,
        audience=audience,
        grant_type="urn:ietf:params:oauth:grant-type:jwt-bearer",
        assertion=token,
    )

    return jsonify(token_info)


@app.route("/api/data")
@jwt_required()
def get_data():
    db = get_db()
    collection = db.processed_articles
    cursor = collection.find({})
    data_list = list(cursor)
    return json_util.dumps(data_list)


@app.route("/api/news")
@jwt_required()
def get_news():
    news_client = GuardianClient()
    articles = news_client.search_news('long-covid')
    return jsonify(articles)


@app.route("/api/reddit")
@jwt_required()
def get_reddit_data():
    token = request.headers.get("Authorization").split(" ")[1]

    print("JWT payload:", token)

    reddit_client = RedditClient()
    posts = reddit_client.load_posts()
    return jsonify(posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
