from mongomock import MongoClient
import pandas as pd
import pytest
from src.data_processor import DataProcessor


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

    data_processor = DataProcessor(test_database, test_collection_name)
    assert isinstance(data_processor.df, pd.DataFrame)
    assert len(data_processor.df) > 0


@pytest.fixture
def data_processor(test_database):  # ADDED: data_processor fixture
    test_collection_name = "long_covid_articles"
    return DataProcessor(test_database, test_collection_name)


def test_clean_data(test_df, data_processor):
    test_database = MongoClient().db
    test_collection_name = "long_covid_articles"
    data_processor = DataProcessor(test_database, test_collection_name)
    data_processor.df = test_df
    data_processor.clean_data()

    processed_df = data_processor.df
    assert len(processed_df) == 2
    assert 'publication_date' in processed_df.columns
    assert not processed_df.duplicated(subset=['title']).any()


def test_standardize_date():
    date1 = '2021 Aug 05'
    source1 = 'pubmed'
    assert DataProcessor.standardize_date(
        None, date1, source1) == '2021-Aug-05'

    date2 = 'Published 10 Mar 2022'
    source2 = 'BMJ'
    assert DataProcessor.standardize_date(
        None, date2, source2) == '2022-Mar-10'

    date3 = '2020 July 20'
    source3 = 'other'
    assert DataProcessor.standardize_date(None, date3, source3) is None
