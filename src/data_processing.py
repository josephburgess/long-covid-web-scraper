import pandas as pd
import re


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    df = df.dropna()

    for i, row in df.iterrows():
        standardized_date = standardize_date(
            row['publication_date'], row['source'])
        df.at[i, 'publication_date'] = standardized_date

    df = df.drop_duplicates(subset=['title'])
    df = df.drop(columns=['source'])

    return df


def standardize_date(date_string, source):
    if source == "pubmed":
        date_match = re.search(r'(\d{4}) (\w{3}) (\d{2})', date_string)
        if date_match:
            year = date_match.group(1)
            month = date_match.group(2)
            day = date_match.group(3)
            return f"{year}-{month}-{day}"
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
    file_path = 'data/raw/long_covid_articles.csv'
    df = load_data(file_path)
    processed_df = clean_data(df)
    processed_df.to_csv('data/processed/processed_articles.csv', index=False)


if __name__ == "__main__":
    main()
