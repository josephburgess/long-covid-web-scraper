import logging
import praw
import os
from dotenv import load_dotenv
load_dotenv()


class RedditClient:
    def __init__(self):
        self.client_id = os.getenv('REDDIT_CLIENT_ID')
        self.client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        self.user_agent = os.getenv('REDDIT_USER_AGENT')
        self.subreddit_name = 'covidlonghaulers'
        self.search_terms = [
            'skin', 'burning', 'neurologist', 'neurology', 'fatigue',
            'neuropathy', 'tingling', 'burn', 'fire', 'neuro',
            'sfn', 'sensitive', 'touch', 'POTS'
        ]

    def load_posts(self):
        try:
            reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent
            )
            subreddit = reddit.subreddit(self.subreddit_name)
            search_query = ' OR '.join(
                f'selftext:{term} OR title:{term}' for term in self.search_terms)
            search_results = subreddit.search(
                search_query, time_filter='month')
            output = [{
                'title': post.title,
                'url': post.url,
            } for post in search_results if post.is_self]
            return output
        except Exception as e:
            logging.exception(f'Error loading posts: {e}')
            return None
