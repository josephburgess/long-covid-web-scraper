from ..clients import RedditClient

if __name__ == "__main__":
    client = RedditClient()
    client.gather_gpt_training_data()
