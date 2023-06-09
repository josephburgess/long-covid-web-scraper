from unittest.mock import Mock, MagicMock


def get_mock_comments(body):
    mock_comments = MagicMock()
    mock_comments.replace_more = Mock()
    mock_comments.__iter__.return_value = iter([Mock(body=body)])
    return mock_comments


def setup_mock_reddit(mock_reddit, mock_posts, search=True, submission_ids=None):
    mock_subreddit = MagicMock()
    mock_reddit.return_value.subreddit.return_value = mock_subreddit

    if search:
        mock_subreddit.search.return_value = mock_posts
    else:
        mock_subreddit.top.return_value = mock_posts

    if submission_ids:

        def submission_side_effect(submission_id):
            for post in mock_posts:
                if post.id == submission_id:
                    return post

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

mock_guardian_response = {
    "response": {
        "results": [
            {
                "webUrl": "https://www.example.com/article1",
                "fields": {
                    "headline": "Example Article 1",
                    "thumbnail": "https://www.example.com/thumbnail1",
                    "standfirst": "This is an example article",
                },
                "webPublicationDate": "2023-04-03T13:37:48Z",
            },
            {
                "webUrl": "https://www.example.com/article2",
                "fields": {
                    "headline": "Example Article 2",
                    "thumbnail": "",
                    "standfirst": "",
                },
                "webPublicationDate": "2023-04-03T15:37:48Z",
            },
        ]
    }
}

mock_guardian_client_output = [
    {
        "webUrl": "https://www.example.com/article1",
        "headline": "Example Article 1",
        "thumbnail": "https://www.example.com/thumbnail1",
        "standfirst": "This is an example article",
        "date": "2023-04-03T13:37:48Z",
    },
    {
        "webUrl": "https://www.example.com/article2",
        "headline": "Example Article 2",
        "thumbnail": "",
        "standfirst": "",
        "date": "2023-04-03T15:37:48Z",
    },
]
