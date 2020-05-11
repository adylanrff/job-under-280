import os
from datetime import datetime
from dotenv import load_dotenv
from argparser import get_arguments
from db import initialize_db
from service import TweetService, JobService
from twitter.twitter_api import TwitterAPI
from jobs.hackernews import HackerNewsAPI 
# Models bases
from twitter.model import TweetBase
from jobs.model import JobBase

# Load environment variables
load_dotenv()

# Initialize Twitter API
# print("Initializing Twitter API...")
# twitter_api = TwitterAPI()

# # Initialize Database
print("Initializing DB...")
db_uri = os.getenv("DB_URI")
model_bases = [TweetBase, JobBase]
session = initialize_db(db_uri, model_bases)

# # Initialize Services
# print("Initializing Services...")
# tweet_service = TweetService(session, twitter_api)
# job_service = JobService(session, twitter_api)

if __name__ == "__main__":
    args = get_arguments()
    start_time = datetime.now()

    if args.tweet:
        print("Tweeting...")
        tweet_service.tweet_job()
    elif args.scrap_job:
        print("Scrapping jobs....")
        job_service.scrap_jobs()

    end_time = datetime.now()
    duration = end_time - start_time
    print("Time elapsed: {} seconds".format(duration.seconds))
    

    
    