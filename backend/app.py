from flask import Flask
from flask_cors import CORS
from src.routes import routes
import os


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.bp)
    CORS(app)
    return app


def run_flask_app():
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    run_flask_app()
