import os
from jobs.hackernews import HackerNewsAPI
from jobs.github import GithubAPI
from jobs.model import Job
from service.service import Service

class JobService(Service):
    def __init__(self, session, twitter_api):
        super().__init__(session)
        self.twitter_api = twitter_api

    def _filter_existing_jobs(self, fetched_jobs):
        existing_jobs = self.session.query(Job).filter(Job.job_id_external.in_([job.job_id_external for job in fetched_jobs]))
        exisiting_job_ids = [job.job_id_external for job in existing_jobs]
        new_jobs = [job for job in fetched_jobs if job.job_id_external not in exisiting_job_ids]

        return new_jobs

    def _scrap_hacker_news(self):
        hackernews_jobs = HackerNewsAPI.fetch_all_jobs()
        return self._filter_existing_jobs(hackernews_jobs)

    def _scrap_github(self):
        github_jobs = GithubAPI.fetch_jobs()
        return self._filter_existing_jobs(github_jobs)

    def scrap_jobs(self):
        hackernews_new_jobs = self._scrap_hacker_news()
        github_jobs = self._scrap_github()

        new_jobs = hackernews_new_jobs+github_jobs

        try:
            self.session.add_all(new_jobs)
            self.session.commit()

            print("Found {} new jobs".format(len(new_jobs)))
            self.twitter_api.report("Scrapped jobs: found {} new jobs".format(len(new_jobs)))
        except Exception as e:
            print("ERROR: ", e)
