import pandas as pd
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.database import DatabaseManager
from src.database import get_db
from .wordcloud_filtered_words import custom_filter_words


class DataProcessor:
    def __init__(self, db, collection_name):
        self.db = db
        self.collection_name = collection_name
        self.df = self.load_data()
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def load_data(self):
        collection = self.db[self.collection_name]
        data = list(collection.find())
        return pd.DataFrame(data)

    def clean_data(self):
        print("Cleaning data...")
        self.df = self.df.dropna()

        for i, row in self.df.iterrows():
            standardized_date = self.standardize_date(
                row["publication_date"], row["source"]
            )
            self.df.at[i, "publication_date"] = standardized_date

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

    def extract_top_words(self, top_n=120):
        word_counter = Counter()

        for _, row in self.df.iterrows():
            text = row["title"] + " " + row["summary"]
            words = re.findall(r"\b\w+\b", text.lower())

            for word in words:
                if word not in self.stop_words and word not in custom_filter_words and not word.isdigit():
                    lemmatized_word = self.lemmatizer.lemmatize(word)
                    word_counter.update([lemmatized_word])

        top_words = word_counter.most_common(top_n)

        result = [{"text": word, "value": count} for word, count in top_words]

        top_words_collection = self.db["top_words"]
        top_words_collection.delete_many({})
        top_words_collection.insert_many(result)

        return result


    def get_filtered_words(self, text):
        words = re.findall(r"\b\w+\b", text.lower())
        filtered_words = [
            self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words
        ]
        return filtered_words

    def update_word_counter(self, word_counter, text):
        filtered_words = self.get_filtered_words(text)
        word_counter.update(filtered_words)




def main():
    db = get_db()
    data_processor = DataProcessor(db, "articles")
    data_processor.clean_data()
    data_processor.update_processed_collection("processed_articles")
    data_processor.extract_top_words()
    print(
        f"{data_processor.new_articles_count} new articles processed and added to the 'processed_articles' database."
    )


if __name__ == "__main__":
    main()
