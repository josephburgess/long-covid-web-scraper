from bson.objectid import ObjectId
from db_connector import get_db


class DatabaseManager:
    def __init__(self, collection_name: str):
        self.db = get_db()
        self.collection = self.db[collection_name]

    def _get_existing_article_ids(self):
        existing_articles = self.collection.find({}, {'_id': 1})
        return set([article['_id'] for article in existing_articles])

    def _deduplicate_articles(self, new_articles):
        seen_ids = self._get_existing_article_ids()
        deduplicated_articles = []

        for article in new_articles:
            if '_id' not in article:
                article['_id'] = ObjectId()

            if article['_id'] not in seen_ids:
                deduplicated_articles.append(article)

        return deduplicated_articles

    def update_collection(self, new_articles):
        deduplicated_articles = self._deduplicate_articles(new_articles)

        if deduplicated_articles:
            self.collection.insert_many(deduplicated_articles)
