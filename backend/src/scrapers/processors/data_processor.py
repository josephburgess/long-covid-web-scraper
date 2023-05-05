import pandas as pd
import re
from src.database import DatabaseManager
from src.database import get_db
from alive_progress import alive_bar, animations


class DataProcessor:
    def __init__(self, db, collection_name):
        self.db = db
        self.collection_name = collection_name
        self.df = self.load_data()

    def load_data(self):
        collection = self.db[self.collection_name]
        data = list(collection.find())
        return pd.DataFrame(data)

    def clean_data(self):
        print("Cleaning data...")
        self.df = self.df.dropna()
        with alive_bar(len(self.df)) as bar:
            for i, row in self.df.iterrows():
                standardized_date = self.standardize_date(
                    row["publication_date"], row["source"]
                )
                self.df.at[i, "publication_date"] = standardized_date
                bar()

        self.df = self.df.drop_duplicates(subset=["title"])
        self.df = self.df.dropna(subset=["publication_date"])

    def standardize_date(self, date_string, source):
        if source == "pubmed":
            return self.standardize_pubmed_date(date_string)
        elif source == "BMJ":
            return self.standardize_bmj_date(date_string)
        elif source == "The Lancet":
            return self.standardize_lancet_date(date_string)
        return None

    def standardize_pubmed_date(self, date_string):
        date_match = re.search(r"(\d{4})\s([a-zA-Z]{3})\s(\d{1,2})", date_string)
        if date_match:
            year, month, day = date_match.groups()
            return f"{year}-{month}-{day.zfill(2)}"

    def standardize_bmj_date(self, date_string):
        date_match = re.search(r"Published (\d{2}) (\w{3}) (\d{4})", date_string)
        if date_match:
            day, month, year = date_match.groups()
            return f"{year}-{month}-{day}"

    def standardize_lancet_date(self, date_string):
        date_match = re.search(
            r"Published: ([a-zA-Z]+) (\d{1,2}), (\d{4})", date_string
        )
        if date_match:
            month, day, year = date_match.groups()
            return f"{year}-{month[:3]}-{day.zfill(2)}"

    def update_processed_collection(self, processed_collection_name):
        db_manager = DatabaseManager(processed_collection_name)
        db_manager.update_collection(self.df.to_dict(orient="records"))
        self.new_articles_count = db_manager.new_articles_count


def main():  # pragma: no cover
    print('Processing "articles" collection...')
    db = get_db()
    data_processor = DataProcessor(db, "articles")
    data_processor.clean_data()
    data_processor.update_processed_collection("processed_articles")
    print(
        f"{data_processor.new_articles_count} new articles processed and added to the 'processed_articles' database."
    )


if __name__ == "__main__":
    main()
