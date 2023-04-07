import pandas as pd
import re
from datetime import datetime
from scrapers import DatabaseManager
from db_connector import get_db


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
        self.df = self.df.dropna()

        for i, row in self.df.iterrows():
            standardized_date = self.standardize_date(
                row['publication_date'], row['source'])
            self.df.at[i, 'publication_date'] = standardized_date

        self.df = self.df.drop_duplicates(subset=['title'])
        self.df = self.df.dropna(subset=['publication_date'])

    def standardize_date(self, date_string, source):
        if source == 'pubmed':
            date_match = re.search(
                r'(\d{4})\s([a-zA-Z]{3})\s(\d{1,2})', date_string)
            if date_match:
                year, month, day = date_match.groups()
                return f'{year}-{month}-{day.zfill(2)}'
        elif source == "BMJ":
            date_match = re.search(
                r'Published (\d{2}) (\w{3}) (\d{4})', date_string)
            if date_match:
                day = date_match.group(1)
                month = date_match.group(2)
                year = date_match.group(3)
                return f"{year}-{month}-{day}"
        elif source == "The Lancet":
            date_match = re.search(
                r'Published: ([a-zA-Z]+) (\d{1,2}), (\d{4})', date_string)
            if date_match:
                month, day, year = date_match.groups()
                return f'{year}-{month[:3]}-{day.zfill(2)}'
        return None

    def update_processed_collection(self, processed_collection_name):
        db_manager = DatabaseManager(processed_collection_name)
        db_manager.update_collection(self.df.to_dict(orient='records'))


def main():
    db = get_db()
    data_processor = DataProcessor(db, 'articles')
    data_processor.clean_data()
    data_processor.update_processed_collection('processed_articles')


if __name__ == "__main__":
    main()
