"""
This module provides a simple client for fetching and processing posts from Reddit.
It includes a RedditClient class with methods to retrieve search results, gather GPT 
training data, and process individual submissions.
"""

import logging
import os
import json
import praw
import requests
from dotenv import load_dotenv

load_dotenv()


class RedditClient:
    """
    A simple client class for interacting with the Reddit API.
    Attributes:
    - client_id (str): Reddit API client ID, retrieved from environment variables.
    - client_secret (str): Reddit API client secret, retrieved from environment variables.
    - user_agent (str): Reddit API user agent, retrieved from environment variables.
    - subreddit_name (str): The subreddit from which to fetch posts.
    - search_terms (List[str]): The search terms to filter posts.
    """

    def __init__(self, search_terms=None):
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")
        self.subreddit_name = "covidlonghaulers"
        self.search_terms = search_terms

    def _get_reddit_instance(self):
        return praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        )

    def load_posts(self):
        """
        Retrieves search results for posts on the specified subreddit.
        Returns:
        - list[dict]: A list of dictionaries containing the search results, None if an error occurs.
        """
        try:
            search_results = self._fetch_search_results()
            return self._extract_output(search_results)
        except requests.RequestException as error:
            logging.exception("Error loading posts: %s", error)
            return None

    def gather_gpt_training_data(self):
        """
        Retrieves search results for posts on the specified subreddit and processes them into a format
        suitable for training a GPT model.
        Returns:
        - list[str]: A list of strings containing the processed search results, None if an error occurs.
        """
        try:
            submission_ids = self._fetch_submission_ids()
            data = self._process_submissions(submission_ids)
            self._write_to_file("reddit_data.jsonl", data)
        except requests.RequestException as error:
            logging.exception("Error loading data: %s", error)
            return None

    def _build_search_query(self):
        return " OR ".join(
            f"selftext:{term} OR title:{term}" for term in self.search_terms
        )

    def _fetch_search_results(self):
        reddit = self._get_reddit_instance()
        subreddit = reddit.subreddit(self.subreddit_name)

        if self.search_terms:
            search_query = self._build_search_query()
            return subreddit.search(search_query, sort="new", time_filter="month")
        else:
            return subreddit.top("week")

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
        print(submission.title)
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
        with open(file_name, "w", encoding="utf-8") as file:
            for item in data:
                file.write(json.dumps(item) + "\n")
