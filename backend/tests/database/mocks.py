import mongomock


def mock_get_db():
    client = mongomock.MongoClient()
    db = client.test_db
    return db
