from pymongo import MongoClient
from bson.objectid import ObjectId
import os


def update_mongodb_collection(collection_name, new_articles):
    mongo_url = os.getenv('MONGO_CLIENT_STRING', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_url)
    db = client.longcovid
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
    client.close()
