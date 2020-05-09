from crontab import CronTab
import getpass

user = getpass.getuser()
print("Setting cron for user: {}".format(user))

cron = CronTab(user=user)
# Clear all jobs
cron.remove_all()

# Set tweet job every 30 minutes
tweet_job = cron.new("python3 jobs-under-280/core.py --tweet", comment="Tweet Jobs")
tweet_job.minute.every(15)

# Set scrap jobs daily
scrap_job = cron.new("python3 jobs-under-280/core.py --scrap_job", comment="Scrap jobs from HN & AngelList")
scrap_job.hour.on(13)  
scrap_job.hour.also.on(1) # Set to * 2,*/10 * * *

cron.write()