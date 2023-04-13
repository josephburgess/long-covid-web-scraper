from src.database import get_db
from bson import json_util


def get_research_data():
    db = get_db()
    collection = db.processed_articles
    cursor = collection.find({}).sort("publication_date", -1)
    data_list = list(cursor)
    return json_util.dumps(data_list, default=json_util.default)
