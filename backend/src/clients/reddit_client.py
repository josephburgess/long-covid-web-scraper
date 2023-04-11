# reddit_client.py

import logging
import praw
from .reddit_helpers import *


class RedditClient:
    def __init__(self):
        self.client_id, self.client_secret, self.user_agent = load_credentials()
        self.subreddit_name = "covidlonghaulers"
        self.search_terms = [
            "skin",
            "burning",
            "neurologist",
            "neurology",
            "fatigue",
            "neuropathy",
            "tingling",
            "burn",
            "fire",
            "neuro",
            "sfn",
            "sensitive",
            "touch",
            "POTS",
        ]

    def _get_reddit_instance(self):
        return praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        )

    def load_posts(self):
        try:
            search_results = fetch_search_results(self)
            return extract_output(search_results)
        except Exception as e:
            logging.exception(f"Error loading posts: {e}")
            return None

    def gather_gpt_training_data(self):
        try:
            submission_ids = fetch_submission_ids(self)
            data = process_submissions(self, submission_ids)
            write_to_file("reddit_data.jsonl", data)
        except Exception as e:
            logging.exception(f"Error loading data: {e}")
            return None
