import datetime
import logging
import time

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("schedule")
logger.setLevel(level=logging.DEBUG)


def check_mentions(api, query, message):
    # sourcery skip: use-assigned-variable
    logger.info("Retrieving mentions")
    api.get_me().data.id
    for tweets in api.search_recent_tweets(
        query=query,
        max_results=100,
        expansions=[
            "author_id",
            "in_reply_to_user_id",
            "entities.mentions.username",
            "referenced_tweets.id.author_id",
        ],
    ):
        for tweet in tweets:
            if tweet is None:
                continue
            if len(tweet) == 0:
                continue
            if len(tweet) != 0 and "Could not find user with id" in tweet.get(
                "detail", ""
            ):
                continue
            # if tweet.in_reply_to_status_id is not None:
            #     continue

            author_data = api.get_user(id=tweet.author_id)
            # following = api.follow_user(tweet.author_id)
            logger.info(f"Answering to {author_data.data.name}")

            # if not following.data.get("following"):
            #     api.follow_user(tweet.author_id)

            api.create_tweet(
                text=message,
                in_reply_to_tweet_id=tweet.id,
            )
            time.sleep(60)


def main():
    api = create_api()
    while True:
        check_mentions(
            api=api,
            query="(cachorro OR cão OR gato OR amo meu cachorro OR amo meu gato) -oferta -relâmpago lang:pt",
            message=f"Aproveite o benefício de R$30 OFF + DOBRO de ITENS no 1º mês e LAMBE LAMBE e PUSH BALL no 2º mês de assinatura com meu cupom! https://box.petiko.com.br/cupom/PETUNIA \n\n #boxpetiko {datetime.datetime.now().strftime('%d %b %Y %H:%M:%S')}",
        )
        logger.info("Waiting...")


if __name__ == "__main__":
    main()
