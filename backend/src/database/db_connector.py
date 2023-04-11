from pymongo import MongoClient
import os


def get_db():
    mongo_url = os.getenv('MONGO_CLIENT_STRING', 'mongodb://0.0.0.0')
    client = MongoClient(mongo_url)
    db = client.longcovid
    return db
