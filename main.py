import utils
import twitter
import tweepy
import json
import threading

def main():
    logger = utils.Logger("MAIN")
    try:
        config_file = open("config.json", "r")
        config = json.load(config_file)
        consumer_key = config["consumer_key"]
        consumer_secret = config["consumer_secret"]
        access_token = config["access_token"]
        access_token_secret = config["access_token_secret"]
        logger.success("Credentials loaded.")
    except Exception as e:
        logger.error(f"Failed loading config.json: {e}")

    try:
        logger.info("Initializing API...")
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        logger.success("Initialization successful!")
    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        return

    try:
        threads = []
        for user in config["users"]:
            thread = threading.Thread(target=twitter.TwitterUser, args=(user["user"], config["delay_seconds"], user["lang"], user["replies"], api))
            threads.append(thread)
            thread.start()
            logger.success(f"Thread started for user: {user['user']}")
    except Exception as e:
        logger.error(f"Error running main.py: {e}")

if __name__ == "__main__":
    main()