from pymongo import MongoClient
import pandas as pd
import re
import os
from scrapers import update_mongodb_collection
from db_connector import get_db


def load_data(db, collection_name):
    collection = db[collection_name]
    data = list(collection.find())
    df = pd.DataFrame(data)
    return df


def clean_data(df):
    df = df.dropna()

    for i, row in df.iterrows():
        standardized_date = standardize_date(
            row['publication_date'], row['source'])
        df.at[i, 'publication_date'] = standardized_date

    df = df.drop_duplicates(subset=['title'])
    df = df.dropna(subset=['publication_date'])
    return df


def standardize_date(date_string, source):
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
    return None


def main():
    db = get_db()
    df = load_data(db, 'long_covid_articles')
    processed_df = clean_data(df)
    collection_name = 'processed_articles'
    update_mongodb_collection(
        collection_name, processed_df.to_dict(orient='records'))


if __name__ == "__main__":
    main()
