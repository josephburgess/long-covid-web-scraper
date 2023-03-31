from unittest.mock import Mock, patch
from src.clients import RedditClient


def test_load_posts():
    mock_post1 = Mock(title='Post 1', url='https://www.reddit.com/post1')
    mock_post2 = Mock(title='Post 2', url='https://www.reddit.com/post2')
    mock_search_results = [mock_post1, mock_post2]

    mock_reddit = Mock()
    mock_reddit.subreddit.return_value.search.return_value = mock_search_results
    with patch('praw.Reddit', return_value=mock_reddit):
        client = RedditClient()
        posts = client.load_posts()

    expected_output = [
        {'title': 'Post 1', 'url': 'https://www.reddit.com/post1'},
        {'title': 'Post 2', 'url': 'https://www.reddit.com/post2'}
    ]
    assert posts == expected_output
