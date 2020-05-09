import os
from datetime import datetime
from dotenv import load_dotenv
from argparser import get_arguments
from db import initialize_db, Base
from service import TweetService, JobService
from twitter.twitter_api import TwitterAPI
from twitter.model import Tweet
from jobs.model import Job
from jobs.hackernews import HackerNewsAPI 

# Load environment variables
load_dotenv()

# Initialize Twitter API
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
db_uri = os.getenv("DB_URI")

twitter_api = TwitterAPI(consumer_key, \
    consumer_secret, 
    access_token, 
    access_token_secret)

# Initialize Database
session = initialize_db(db_uri)

# Initialize Services
tweet_service = TweetService(session, twitter_api)
job_service = JobService(session)

if __name__ == "__main__":
    args = get_arguments()
    if args.tweet:
        # do tweet here
        pass
    elif args.scrap_job:
        print("Scrapping jobs....")
        start_time = datetime.now()
        job_service.scrap_jobs()
        end_time = datetime.now()
        duration = end_time - start_time
        print("Time elapsed: {} seconds".format(duration.seconds))

    
    