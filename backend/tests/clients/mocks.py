from unittest.mock import Mock, MagicMock


def get_mock_comments(body):
    mock_comments = MagicMock()
    mock_comments.replace_more = Mock()
    mock_comments.__iter__.return_value = iter([Mock(body=body)])
    return mock_comments


def setup_mock_reddit(mock_reddit, mock_posts, submission_ids=None):
    mock_reddit.return_value.subreddit.return_value.search.return_value = mock_posts

    if submission_ids:

        def submission_side_effect(id):
            post = next(p for p in mock_posts if p.id == id)
            mock_submission = Mock()
            mock_submission.title = post.title
            mock_submission.selftext = post.selftext
            mock_submission.comments = post.comments
            return mock_submission

        mock_reddit.return_value.submission.side_effect = submission_side_effect


mock_comments1 = get_mock_comments("Answer to the first question.")
mock_comments2 = get_mock_comments("Answer to the second question.")

mock_reddit_posts = [
    Mock(
        id="1",
        title="Post 1",
        url="https://www.reddit.com/post1",
        created_utc=1617000000.0,
        selftext="This is test text for the first reddit post",
        is_self=True,
        comments=mock_comments1,
    ),
    Mock(
        id="2",
        title="Post 2",
        url="https://www.reddit.com/post2",
        created_utc=1617100000.0,
        selftext="This is test text for the second reddit post",
        is_self=True,
        comments=mock_comments2,
    ),
    Mock(
        id="3",
        title="Non-self Post",
        url="https://www.reddit.com/nonselfpost",
        created_utc=1617200000.0,
        selftext="",
        is_self=False,
    ),
]
