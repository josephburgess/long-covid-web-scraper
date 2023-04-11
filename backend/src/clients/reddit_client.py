import logging
import os
import json
import praw
from dotenv import load_dotenv

load_dotenv()


class RedditClient:
    def __init__(self):
        self._load_credentials()
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

    def _load_credentials(self):
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")

    def _get_reddit_instance(self):
        return praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        )

    def load_posts(self):
        try:
            search_results = self._fetch_search_results()
            return self._extract_output(search_results)
        except Exception as e:
            logging.exception(f"Error loading posts: {e}")
            return None

    def gather_gpt_training_data(self):
        try:
            submission_ids = self._fetch_submission_ids()
            data = self._process_submissions(submission_ids)
            self._write_to_file("reddit_data.jsonl", data)
        except Exception as e:
            logging.exception(f"Error loading data: {e}")
            return None

    def _build_search_query(self):
        return " OR ".join(
            f"selftext:{term} OR title:{term}" for term in self.search_terms
        )

    def _fetch_search_results(self):
        search_query = self._build_search_query()
        reddit = self._get_reddit_instance()
        subreddit = reddit.subreddit(self.subreddit_name)
        return subreddit.search(search_query, sort="new", time_filter="month")

    def _extract_output(self, search_results):
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

    def _fetch_submission_ids(self):
        reddit = self._get_reddit_instance()
        subreddit = reddit.subreddit(self.subreddit_name)
        return [
            submission.id
            for submission in subreddit.search(
                query="flair:Question", sort="top", time_filter="all", limit=500
            )
        ]

    def _process_submissions(self, submission_ids):
        reddit = self._get_reddit_instance()
        return [
            data
            for id in submission_ids
            for data in self._process_single_submission(reddit.submission(id))
        ]

    def _process_single_submission(self, submission):
        submission.comments.replace_more(limit=0)
        data = []

        for comment in submission.comments:
            if self._is_comment_valid(comment):
                prompt = f"{submission.title} {submission.selftext}"
                data.append(
                    {
                        "prompt": prompt,
                        "completion": comment.body,
                    }
                )
                break

        return data

    @staticmethod
    def _is_comment_valid(comment):
        return comment.body and comment.body != "[deleted]"

    @staticmethod
    def _write_to_file(file_name, data):
        with open(file_name, "w") as f:
            for item in data:
                f.write(json.dumps(item) + "\n")
