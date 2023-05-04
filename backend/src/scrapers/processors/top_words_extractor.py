import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from .wordcloud_filtered_words import custom_filter_words
from src.database import get_db
from .data_processor import DataProcessor
from alive_progress import alive_bar, animations


class TopWordsExtractor:
    def __init__(self, db, df):
        self.db = db
        self.df = df
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def extract_top_words(self, top_n=120):
        word_counter = Counter()

        with alive_bar(len(self.df)) as bar:
            for _, row in self.df.iterrows():
                text = row["title"] + " " + row["summary"]
                words = re.findall(r"\b\w+\b", text.lower())
                filtered_words = self.process_words(words)
                word_counter.update(filtered_words)
                bar()

        top_words = word_counter.most_common(top_n)
        result = [{"text": word, "value": count} for word, count in top_words]

        top_words_collection = self.db["top_words"]
        top_words_collection.delete_many({})
        top_words_collection.insert_many(result)

        return result

    def is_valid_word(self, word):
        return (
            word not in self.stop_words
            and word not in custom_filter_words
            and not word.isdigit()
        )

    def process_words(self, words):
        return [
            self.lemmatizer.lemmatize(word)
            for word in words
            if self.is_valid_word(word)
        ]

    def get_filtered_words(self, text):
        words = re.findall(r"\b\w+\b", text.lower())
        filtered_words = [
            self.lemmatizer.lemmatize(word)
            for word in words
            if word not in self.stop_words
        ]
        return filtered_words

    def update_word_counter(self, word_counter, text):
        filtered_words = self.get_filtered_words(text)
        word_counter.update(filtered_words)


def main():  # pragma: no cover
    print("Extracting top words...")
    db = get_db()
    data_processor = DataProcessor(db, "processed_articles")
    df = data_processor.load_data()

    top_words_extractor = TopWordsExtractor(db, df)
    top_words = top_words_extractor.extract_top_words(top_n=120)

    print("Top words extracted!")


if __name__ == "__main__":
    main()
