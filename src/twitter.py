import time
import utils
import translate as t
import re


class TwitterUser:
    def __init__(self, user, delay_seconds, target_lang, replies, api):
        self.user = user
        self.delay_seconds = delay_seconds
        self.logger = utils.Logger("USER", user)
        self.api = api
        self.id = None
        self.text = None
        self.target_lang = target_lang
        self.tweet_lang = None
        if replies:
            self.replies = True
        else:
            self.replies = False
        self.run()

    def initialize(self):
        self.logger.info("Initializing monitor...")
        try:
            tweets = self.api.user_timeline(screen_name=self.user, count=1,
                                            include_rts=True)
            if tweets:
                self.id = tweets[0]._json["id_str"]
                self.text = tweets[0]._json["text"]
                self.tweet_lang = tweets[0]._json["lang"]
            self.logger.success("User initialized!")
            self.monitor()
        except IndexError:
            self.logger.alert("Failed to initialize user.")

    def cycle(self):
        self.logger.info("Monitoring...")
        tweets_obj = self.api.user_timeline(screen_name=self.user,
                                            count=1, include_rts=True)
        if tweets_obj:
            tweets = tweets_obj[0]._json
            # Checks every new tweet id
            if tweets["id_str"] != self.id:
                # Gets raw text without t.co links
                regex = r'(https|http)?:\/\/(t.co)(\w|\.|\/|\?|\=|\&|\%)*\b'
                raw_text = re.sub(regex, '', tweets["text"])
                if raw_text != '':
                    # Logic check to see if it should translate a text reply
                    reply = tweets["in_reply_to_status_id"]
                    if reply is not None and self.replies:
                        self.id = tweets["id_str"]
                        self.text = raw_text
                        self.tweet_lang = tweets["lang"]
                        self.logger.success(f"New reply detected: {self.text}")
                        translated = self.translate_tweet(self.text)
                        self.send_tweet(translated)
                    # Logic check for non-replies (Regular tweets and retweets)
                    elif reply is None and not raw_text.startswith("RT @"):
                        self.id = tweets["id_str"]
                        self.text = raw_text
                        self.tweet_lang = tweets["lang"]
                        self.logger.success(f"New tweet detected: {self.text}")
                        translated = self.translate_tweet(self.text)
                        self.send_tweet(translated)

    def monitor(self):
        while True:
            try:
                self.cycle()
            except Exception as e:
                self.logger.error(f"Error:\n{e}")
            time.sleep(self.delay_seconds)

    def translate_tweet(self, raw_text):
        if self.tweet_lang != self.target_lang:
            try:
                translated_text = t.translate_text(self.target_lang, raw_text)
                self.logger.info(f"Translated text: {translated_text}")
                return translated_text
            except Exception as e:
                self.logger.error(f"Tweet could not be translated.\n{e}")
        else:
            self.logger.alert("New tweet already in translated language.")

    def send_tweet(self, text):
        try:
            self.api.update_status(text, in_reply_to_status_id=self.id,
                                   auto_populate_reply_metadata=True)
            self.logger.success(f"Sent translated tweet: {text}")
        except Exception as e:
            self.logger.error(f"Failed to send translated tweet.\n{e}")

    def run(self):
        try:
            self.initialize()
        except Exception as e:
            self.logger.error(f"Error:\n{e}")
