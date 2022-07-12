import logging
import os

import tweepy
from dotenv import find_dotenv, load_dotenv

logger = logging.getLogger()
load_dotenv(find_dotenv())


def create_api():
    baerer_token = os.environ.get("BAERER_TOKEN")
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    # set_trace()

    try:
        api = tweepy.Client(
            bearer_token=baerer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True,
        )

    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
