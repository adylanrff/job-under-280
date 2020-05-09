import os
from dotenv import load_dotenv
from lib.twitter import TwitterAPI

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    consumer_key = os.getenv("API_KEY")
    consumer_secret = os.getenv("API_SECRET_KEY")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    twitter_api = TwitterAPI(consumer_key, \
        consumer_secret, 
        access_token, 
        access_token_secret)
    
    twitter_api.tweet("Hello World")