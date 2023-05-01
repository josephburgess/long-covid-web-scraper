from src.database import get_db
from bson import json_util


def get_wordcloud_data():
    db = get_db()
    collection = db.top_words
    cursor = collection.find({})
    data_list = list(cursor)
    return json_util.dumps(data_list, default=json_util.default)
