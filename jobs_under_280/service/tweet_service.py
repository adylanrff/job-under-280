from sqlalchemy import desc
from jobs.model import Job
from service.service import Service

class TweetService(Service):
    def __init__(self, session, twitter_api):
        super().__init__(session)
        self.twitter_api = twitter_api

    def get_hashtags(self):
        return '#job #hiring #career'

    def tweet_job(self):
        job_to_tweet = self.session.query(Job)\
            .filter(Job.is_posted != True)\
            .order_by(desc(Job.date))\
            .first()

        if job_to_tweet is not None:
            message = job_to_tweet.title + " \n\n" + job_to_tweet.link + ' ' + self.get_hashtags()
            print("Tweeted: {}".format(message))

            self.twitter_api.tweet(message)
            
            job_to_tweet.is_posted = True
            self.session.commit()
        else:
            print("No new jobs found")
        