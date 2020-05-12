import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
monitoring_twitter_acc = os.getenv("MONITORING_TWITTER_ACC")

class TwitterAPI:
    def __init__(self, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
    
    def tweet(self, status):
        self.api.update_status(status)

    def report(self,  message, user_id=monitoring_twitter_acc):
        self.api.send_direct_message(user_id, message)