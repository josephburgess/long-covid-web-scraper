import unittest
from mongomock import MongoClient
import pandas as pd
from src.scrapers import DataProcessor


class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.test_database = MongoClient().db
        self.test_collection_name = "long_covid_articles"
        self.data_processor = DataProcessor(
            self.test_database, self.test_collection_name
        )

        self.test_df = pd.DataFrame(
            {
                "title": [
                    "Article 1: Long Covid Symptoms",
                    "Article 2: Long Covid Treatment",
                    "Article 3: Long Covid in Children",
                ],
                "summary": [
                    "This article discusses the symptoms of long Covid.",
                    "This article covers the various treatments for long Covid.",
                    "This article explores the impact of long Covid on children.",
                ],
                "publication_date": ["2020 May 10", "Published 15 Jun 2021", None],
                "source": ["pubmed", "BMJ", "pubmed"],
            }
        )

    def test_load_data(self):
        test_collection = self.test_database[self.test_collection_name]
        test_collection.insert_many(
            [
                {
                    "title": "Article 1",
                    "publication_date": "2020 May 10",
                    "source": "pubmed",
                },
                {
                    "title": "Article 2",
                    "publication_date": "Published 15 Jun 2021",
                    "source": "BMJ",
                },
                {"title": "Article 3", "publication_date": None, "source": "pubmed"},
            ]
        )

        self.data_processor.df = self.data_processor.load_data()
        self.assertIsInstance(self.data_processor.df, pd.DataFrame)
        self.assertGreater(len(self.data_processor.df), 0)

    def test_clean_data(self):
        self.data_processor.df = self.test_df
        self.data_processor.clean_data()
        processed_df = self.data_processor.df

        self.assertEqual(len(processed_df), 2)
        self.assertIn("publication_date", processed_df.columns)
        self.assertFalse(processed_df.duplicated(subset=["title"]).any())

    def test_standardize_date(self):
        date1 = "2021 Aug 05"
        source1 = "pubmed"
        self.assertEqual(
            self.data_processor.standardize_date(date1, source1), "2021-Aug-05"
        )

        date2 = "Published 10 Mar 2022"
        source2 = "BMJ"
        self.assertEqual(
            self.data_processor.standardize_date(date2, source2), "2022-Mar-10"
        )

        date3 = "Published: July 20, 2020"
        source3 = "The Lancet"
        self.assertEqual(
            self.data_processor.standardize_date(date3, source3), "2020-Jul-20"
        )

    def test_extract_top_words(self):
        self.data_processor.df = self.test_df
        top_n = 3

        top_words = self.data_processor.extract_top_words(top_n)
        expected_top_words = [
            {"text": "long", "value": 6},
            {"text": "covid", "value": 6},
            {"text": "article", "value": 6},
        ]

        self.assertEqual(len(top_words), top_n)

        for word in top_words:
            word.pop("_id", None)

        top_words = sorted(top_words, key=lambda x: x["text"])
        expected_top_words = sorted(expected_top_words, key=lambda x: x["text"])

        self.assertEqual(top_words, expected_top_words)

        top_words_collection = self.test_database["top_words"]
        top_words_from_db = list(top_words_collection.find())

        self.assertEqual(len(top_words_from_db), top_n)

        for word in top_words_from_db:
            word.pop("_id", None)

        top_words_from_db = sorted(top_words_from_db, key=lambda x: x["text"])

        self.assertEqual(top_words_from_db, expected_top_words)


if __name__ == "__main__":
    unittest.main()
