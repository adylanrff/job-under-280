import os
import getpass
from crontab import CronTab

cwd = os.getcwd()
user = getpass.getuser()
print("Setting cron for user: {}".format(user))

cron = CronTab(user=user)
# Clear all jobs
cron.remove_all()

# Set tweet job every 30 minutes
tweet_job = cron.new("python3 {}/jobs-under-280/core.py --tweet".format(cwd), comment="Tweet Jobs")
tweet_job.hour.during(3, 8) 
tweet_job.hour.also.during(11, 15)
tweet_job.minute.also.every(30)

# Set scrap jobs daily
scrap_job = cron.new("python3 {}/jobs-under-280/core.py --scrap_job".format(cwd), comment="Scrap jobs from HN & AngelList")
scrap_job.every(12).hours() # set to every 12 hours  

cron.write()