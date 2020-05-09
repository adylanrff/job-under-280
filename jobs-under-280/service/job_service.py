import os
from jobs.hackernews import HackerNewsAPI
from jobs.model import Job
from service.service import Service

class JobService(Service):
    def __init__(self, session, twitter_api):
        super().__init__(session)
        self.twitter_api = twitter_api

    def scrap_jobs(self):
        hackernews_jobs = HackerNewsAPI.fetch_all_jobs()
        existing_jobs = self.session.query(Job).filter(Job.job_id.in_([job.job_id for job in hackernews_jobs]))
        exisiting_job_ids = [job.job_id for job in existing_jobs]
        new_jobs = [job for job in hackernews_jobs if job.job_id not in exisiting_job_ids]

        print("Found {} new jobs".format(len(new_jobs)))

        monitoring_twitter_acc = os.getenv("MONITORING_TWITTER_ACC")
        self.twitter_api.send_dm(monitoring_twitter_acc, "Scrapped jobs: found {} new jobs".format(len(new_jobs)))

        self.session.add_all(new_jobs)
        self.session.commit()
        # TODO: Scrap AngelList

