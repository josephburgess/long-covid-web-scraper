from mongomock import MongoClient
import pandas as pd
import pytest
from src.data_processing import load_data, clean_data, standardize_date


@pytest.fixture
def test_df():
    df = pd.DataFrame({
        'title': ['Article 1', 'Article 2', 'Article 3'],
        'publication_date': ['2020 May 10', 'Published 15 Jun 2021', None],
        'source': ['pubmed', 'BMJ', 'pubmed']
    })
    return df


@pytest.fixture
def test_database():
    return MongoClient().db


def test_load_data(test_database):
    test_collection_name = "long_covid_articles"
    test_collection = test_database[test_collection_name]
    test_collection.insert_many([
        {'title': 'Article 1', 'publication_date': '2020 May 10', 'source': 'pubmed'},
        {'title': 'Article 2', 'publication_date': 'Published 15 Jun 2021', 'source': 'BMJ'},
        {'title': 'Article 3', 'publication_date': None, 'source': 'pubmed'}
    ])

    df = load_data(test_database, test_collection_name)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_clean_data(test_df):
    processed_df = clean_data(test_df)
    assert len(processed_df) == 2
    assert 'publication_date' in processed_df.columns
    assert not processed_df.duplicated(subset=['title']).any()


def test_standardize_date():
    date1 = '2021 Aug 05'
    source1 = 'pubmed'
    assert standardize_date(date1, source1) == '2021-Aug-05'

    date2 = 'Published 10 Mar 2022'
    source2 = 'BMJ'
    assert standardize_date(date2, source2) == '2022-Mar-10'

    date3 = '2020 July 20'
    source3 = 'other'
    assert standardize_date(date3, source3) is None
