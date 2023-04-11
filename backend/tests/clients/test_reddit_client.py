from unittest.mock import patch
import unittest
from src.clients import RedditClient
from mocks import mock_reddit_posts, setup_mock_reddit


class TestRedditClient(unittest.TestCase):
    def setUp(self):
        self.mock_posts = mock_reddit_posts

    def test_load_posts(self):
        with patch("praw.Reddit") as mock_reddit:
            setup_mock_reddit(mock_reddit, self.mock_posts, search=False)
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

        self.assertEqual(posts, expected_output)

    def test_gather_gpt_training_data(self):
        with patch("src.clients.RedditClient._write_to_file") as mock_write_to_file:
            with patch("praw.Reddit") as mock_reddit:
                setup_mock_reddit(
                    mock_reddit,
                    self.mock_posts[:2],
                    search=True,
                    submission_ids=["1", "2"],
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

            mock_write_to_file.assert_called_once_with(
                "reddit_data.jsonl", expected_output
            )


if __name__ == "__main__":
    unittest.main()
