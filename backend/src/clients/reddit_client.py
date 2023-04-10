import logging
import os
import json
import praw
from dotenv import load_dotenv

load_dotenv()


class RedditClient:
    def __init__(self):
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")
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
            reddit = self._get_reddit_instance()
            subreddit = reddit.subreddit(self.subreddit_name)
            search_query = " OR ".join(
                f"selftext:{term} OR title:{term}" for term in self.search_terms
            )
            search_results = subreddit.search(
                search_query, sort="new", time_filter="month"
            )
            output = [
                {
                    "title": post.title,
                    "url": post.url,
                    "created": post.created_utc,
                    "selftext": post.selftext,
                }
                for post in search_results
                if post.is_self
            ]
            return output
        except Exception as e:
            logging.exception(f"Error loading posts: {e}")
            return None

    def gather_gpt_training_data(self):
        try:
            reddit = self._get_reddit_instance()
            subreddit = reddit.subreddit(self.subreddit_name)

            data = []
            submission_ids = []

            for submission in subreddit.search(
                query="flair:Question", sort="top", time_filter="all", limit=500
            ):
                submission_ids.append(submission.id)

            for id in submission_ids:
                submission = reddit.submission(id)
                processed_data = self._process_submission(submission)
                if processed_data:
                    data.extend(processed_data)

            self._write_to_file("reddit_data.jsonl", data)

        except Exception as e:
            logging.exception(f"Error loading data: {e}")
            return None

    def _process_submission(self, submission):
        print(submission.title)
        submission.comments.replace_more(limit=0)

        data = []
        for comment in submission.comments:
            if not comment.body or comment.body == "[deleted]":
                continue
            prompt = submission.title + " " + submission.selftext
            data.append({"prompt": prompt, "completion": comment.body})
            if len(data) == 5:
                break
        return data if data else None

    @staticmethod
    def _write_to_file(file_name, data):
        with open(file_name, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
