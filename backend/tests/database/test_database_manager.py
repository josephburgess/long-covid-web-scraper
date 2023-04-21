import pytest
from bson.objectid import ObjectId
from src.database import DatabaseManager
from .mocks import mock_get_db


@pytest.fixture
def test_db_manager(monkeypatch):
    monkeypatch.setattr("src.database.get_db", mock_get_db)
    db_manager = DatabaseManager("test_collection")
    yield db_manager
    db_manager.collection.delete_many({})


def test_existing_article_ids(test_db_manager):
    test_db_manager.collection.insert_one(
        {"_id": ObjectId(), "title": "Test Article 1"}
    )
    test_db_manager.collection.insert_one(
        {"_id": ObjectId(), "title": "Test Article 2"}
    )

    existing_ids = test_db_manager._get_existing_article_ids()
    assert len(existing_ids) == 2


def test_deduplicate_articles(test_db_manager):
    test_db_manager.collection.insert_one(
        {"_id": ObjectId(), "title": "Test Article 1"}
    )
    test_db_manager.collection.insert_one(
        {"_id": ObjectId(), "title": "Test Article 2"}
    )

    new_articles = [
        {
            "_id": list(test_db_manager._get_existing_article_ids())[0],
            "title": "Test Article 1",
        },
        {"title": "Test Article 3"},
    ]

    deduplicated_articles = test_db_manager._deduplicate_articles(new_articles)
    assert len(deduplicated_articles) == 1
    assert deduplicated_articles[0]["title"] == "Test Article 3"


def test_update_collection(test_db_manager):
    new_articles = [
        {"title": "Test Article 1"},
        {"title": "Test Article 2"},
    ]

    test_db_manager.update_collection(new_articles)
    assert test_db_manager.collection.count_documents({}) == 2
    assert test_db_manager.new_articles_count == 2

    new_articles = [
        {
            "_id": list(test_db_manager._get_existing_article_ids())[0],
            "title": "Test Article 1",
        },
        {"title": "Test Article 3"},
    ]

    test_db_manager.update_collection(new_articles)
    assert test_db_manager.collection.count_documents({}) == 3
    assert test_db_manager.new_articles_count == 1
