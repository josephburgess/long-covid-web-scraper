from unittest.mock import Mock, patch
import unittest
from src.clients import RedditClient


class TestRedditClient(unittest.TestCase):
    def setUp(self):
        self.mock_post1 = Mock(
            title='Post 1', url='https://www.reddit.com/post1', created_utc=1617000000.0)
        self.mock_post2 = Mock(
            title='Post 2', url='https://www.reddit.com/post2', created_utc=1617100000.0)
        self.mock_search_results = [self.mock_post1, self.mock_post2]

    def test_load_posts(self):
        mock_reddit = Mock()
        mock_reddit.subreddit.return_value.search.return_value = self.mock_search_results
        with patch('praw.Reddit', return_value=mock_reddit):
            client = RedditClient()
            posts = client.load_posts()

        expected_output = [
            {'title': 'Post 1', 'url': 'https://www.reddit.com/post1',
                'created': 1617000000.0},
            {'title': 'Post 2', 'url': 'https://www.reddit.com/post2',
                'created': 1617100000.0}
        ]
        self.assertEqual(posts, expected_output)


if __name__ == '__main__':
    unittest.main()
