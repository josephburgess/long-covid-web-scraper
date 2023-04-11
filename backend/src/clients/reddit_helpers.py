import os
import json
from dotenv import load_dotenv

load_dotenv()


def load_credentials():
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")
    return client_id, client_secret, user_agent


def build_search_query(search_terms):
    return " OR ".join(f"selftext:{term} OR title:{term}" for term in search_terms)


def fetch_search_results(reddit_client):
    search_query = build_search_query(reddit_client.search_terms)
    reddit = reddit_client._get_reddit_instance()
    subreddit = reddit.subreddit(reddit_client.subreddit_name)
    return subreddit.search(search_query, sort="new", time_filter="month")


def extract_output(search_results):
    return [
        {
            "title": post.title,
            "url": post.url,
            "created": post.created_utc,
            "selftext": post.selftext,
        }
        for post in search_results
        if post.is_self
    ]


def fetch_submission_ids(reddit_client):
    reddit = reddit_client._get_reddit_instance()
    subreddit = reddit.subreddit(reddit_client.subreddit_name)
    return [
        submission.id
        for submission in subreddit.search(
            query="flair:Question", sort="top", time_filter="all", limit=500
        )
    ]


def process_submissions(reddit_client, submission_ids):
    reddit = reddit_client._get_reddit_instance()
    return [
        processed_data
        for id in submission_ids
        if (processed_data := process_submission(reddit.submission(id)))
    ]


def process_submission(submission):
    submission.comments.replace_more(limit=0)
    data = []

    for comment in submission.comments:
        if is_comment_valid(comment):
            prompt = f"{submission.title} {submission.selftext}"
            data.append(
                {
                    "prompt": prompt,
                    "completion": comment.body,
                }
            )
            break

    return data


def is_comment_valid(comment):
    return comment.body and comment.body != "[deleted]"


def write_to_file(file_name, data):
    with open(file_name, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
