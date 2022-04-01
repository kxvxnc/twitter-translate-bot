import utils
import twitter
import tweepy
import json
import threading
import os
from dotenv import load_dotenv


def main():
    logger = utils.Logger("MAIN")
    try:
        load_dotenv()
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        logger.success("Credentials loaded.")
    except Exception as e:
        logger.error(f"Failed loading config.json.\n{e}")

    try:
        logger.info("Initializing API...")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        logger.success("Initialization successful!")
    except Exception as e:
        logger.error(f"Initialization failed.\n{e}")
        return

    try:
        config_file = open("src/config.json", "r")
        config = json.load(config_file)
        threads = []

        for user in config["users"]:
            thread = threading.Thread(target=twitter.TwitterUser, args=(
                user["user"], config["delay_seconds"], user["lang"],
                user["replies"], api))
        threads.append(thread)
        thread.start()
        logger.success(f"Thread started for user: {user['user']}")
    except Exception as e:
        logger.error(f"Error running main.py.\n{e}")


if __name__ == "__main__":
    main()
