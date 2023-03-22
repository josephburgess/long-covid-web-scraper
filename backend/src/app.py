from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def get_data():
    file_path = '../data/processed/processed_articles.csv'
    df = pd.read_csv(file_path)
    json_data = df.to_json(orient='records')
    return json_data


if __name__ == "__main__":
    app.run(debug=True)
