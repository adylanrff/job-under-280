import requests
from jobs.model import Job

GITHUB_JOB_API_URL = "https://jobs.github.com/positions.json"

class GithubAPI:
    @staticmethod
    def fetch_jobs():
        jobs = []
        job_jsons = requests.get(GITHUB_JOB_API_URL).json()
        for job_json in job_jsons:
            job = Job()
            job.job_id_external = job_json['id']
            job.title = job_json['title']
            job.description = job_json['description']
            job.link = job_json['url']
            jobs.append(job)

        return jobs