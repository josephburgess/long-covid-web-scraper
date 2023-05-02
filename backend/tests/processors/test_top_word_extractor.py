import unittest
from mongomock import MongoClient
from collections import Counter
from src.scrapers.processors.top_words_extractor import TopWordsExtractor
from .mocks import mock_df


class TestTopWordsExtractor(unittest.TestCase):
    def setUp(self):
        self.test_database = MongoClient().db
        self.test_collection_name = "long_covid_articles"
        self.top_words_extractor = TopWordsExtractor(self.test_database, mock_df)
        self.test_df = mock_df

    def compare_top_words_lists(self, actual, expected):
        for word in actual:
            word.pop("_id", None)

        actual = sorted(actual, key=lambda x: x["text"])
        expected = sorted(expected, key=lambda x: x["text"])

        return actual == expected

    def test_extract_top_words(self):
        self.top_words_extractor.df = self.test_df
        top_n = 3

        top_words = self.top_words_extractor.extract_top_words(top_n)
        expected_top_words = [
            {"text": "symptom", "value": 2},
            {"text": "infection", "value": 2},
            {"text": "health", "value": 2},
        ]

        self.assertEqual(len(top_words), top_n)
        self.assertTrue(self.compare_top_words_lists(top_words, expected_top_words))

        top_words_collection = self.test_database["top_words"]
        top_words_from_db = list(top_words_collection.find())

        self.assertEqual(len(top_words_from_db), top_n)
        self.assertTrue(
            self.compare_top_words_lists(top_words_from_db, expected_top_words)
        )

    def test_get_filtered_words(self):
        text = "This is a test text containing some stop words like and, the, of"
        expected_filtered_words = ["test", "text", "containing", "stop", "word", "like"]
        self.assertEqual(
            self.top_words_extractor.get_filtered_words(text), expected_filtered_words
        )

    def test_update_word_counter(self):
        word_counter = Counter()
        text = "This is a test text containing some stop words like and, the, of"
        expected_word_counter = Counter(
            {"test": 1, "text": 1, "containing": 1, "stop": 1, "word": 1, "like": 1}
        )
        self.top_words_extractor.update_word_counter(word_counter, text)
        self.assertEqual(word_counter, expected_word_counter)


if __name__ == "__main__":
    unittest.main()
