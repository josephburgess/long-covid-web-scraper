from bson.objectid import ObjectId
from db_connector import get_db


def update_mongodb_collection(collection_name, new_articles):
    db = get_db()
    collection = db[collection_name]

    existing_articles = collection.find({}, {'_id': 1})
    seen_ids = set([article['_id'] for article in existing_articles])

    for article in new_articles:
        if '_id' not in article:
            article['_id'] = ObjectId()

    deduplicated_articles = [
        article for article in new_articles if article['_id'] not in seen_ids]

    if deduplicated_articles:
        collection.insert_many(deduplicated_articles)
