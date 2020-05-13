import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from jobs.model import Job

HACKERNEWS_API_BASE_URL = "https://hacker-news.firebaseio.com/v0/"
HACKERNEWS_API_JOBS_URL = HACKERNEWS_API_BASE_URL + 'jobstories.json'
HACKERNEWS_API_ITEM_URL = HACKERNEWS_API_BASE_URL + '/item/{}.json'

class HackerNewsAPI:
    jobs = []
    @staticmethod
    def fetch_all_jobs():
        job_item_ids = requests.get(HACKERNEWS_API_JOBS_URL).json()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(HackerNewsAPI.fetch_jobs(job_item_ids))
        loop.run_until_complete(future)
        return HackerNewsAPI.jobs

    @staticmethod
    def fetch_job(session, item_id):
        with session.get(HACKERNEWS_API_ITEM_URL.format(item_id)) as response:
            data = response.json()
            if data is not None:
                job = HackerNewsAPI.parse_job(data)
                return job
            return None

    @staticmethod
    async def fetch_jobs(item_ids):
        with ThreadPoolExecutor(max_workers=20) as executor:
            with requests.Session() as session:        
                loop = asyncio.get_event_loop()             

                tasks = [
                    loop.run_in_executor(
                        executor,
                        HackerNewsAPI.fetch_job,
                        *(session, item_id) # Allows us to pass in multiple arguments to `fetch`
                    )
                    for item_id in item_ids
                ]

                # Initializes the tasks to run and awaits their results
                for job in await asyncio.gather(*tasks):
                    if job is not None:
                        HackerNewsAPI.jobs.append(job)


    @staticmethod
    def parse_job(json_resp):
        job = Job()
        job.title = json_resp.get('title', '')
        job.job_id = json_resp.get('id', '')
        job.link = json_resp.get('url', '')
        return job