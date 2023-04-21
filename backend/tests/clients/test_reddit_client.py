import pytest
from unittest.mock import patch
from src.clients import RedditClient
from mocks import mock_reddit_posts, setup_mock_reddit


@pytest.fixture(scope="module")
def mock_posts():
    return mock_reddit_posts


@pytest.fixture
def reddit_client():
    return RedditClient()


def test_load_posts(mock_posts):
    with patch("praw.Reddit") as mock_reddit:
        setup_mock_reddit(mock_reddit, mock_posts, search=False)
        client = RedditClient()
        posts = client.load_posts()

    expected_output = [
        {
            "title": "Post 1",
            "url": "https://www.reddit.com/post1",
            "created": 1617000000.0,
            "selftext": "This is test text for the first reddit post",
        },
        {
            "title": "Post 2",
            "url": "https://www.reddit.com/post2",
            "created": 1617100000.0,
            "selftext": "This is test text for the second reddit post",
        },
    ]

    assert posts == expected_output


def test_build_search_query(reddit_client):
    client = RedditClient(search_terms=["term1", "term2"])
    search_query = client._build_search_query()
    assert (
        search_query == "selftext:term1 OR title:term1 OR selftext:term2 OR title:term2"
    )


def test_search_query_when_search_terms_present(mock_posts):
    with patch(
        "src.clients.RedditClient._fetch_search_results"
    ) as mock_fetch_search_results:
        mock_fetch_search_results.return_value = mock_posts
        client = RedditClient(search_terms=["term1", "term2"])
        client.load_posts()

        mock_fetch_search_results.assert_called_once()


def test_gather_gpt_training_data(mock_posts):
    with patch("src.clients.RedditClient._write_to_file") as mock_write_to_file:
        with patch("praw.Reddit") as mock_reddit:
            setup_mock_reddit(
                mock_reddit, mock_posts[:2], search=True, submission_ids=["1", "2"]
            )
            client = RedditClient()
            client.gather_gpt_training_data()

        expected_output = [
            {
                "prompt": "Post 1 This is test text for the first reddit post",
                "completion": "Answer to the first question.",
            },
            {
                "prompt": "Post 2 This is test text for the second reddit post",
                "completion": "Answer to the second question.",
            },
        ]

        mock_write_to_file.assert_called_once_with("reddit_data.jsonl", expected_output)
