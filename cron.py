from crontab import CronTab
import getpass

user = getpass.getuser()
print("Setting cron for user: {}".format(user))

cron = CronTab(user=user)
# Set tweet job every 30 minutes
tweet_job = cron.new("python jobs-under-280/core.py --tweet", comment="Tweet Jobs")
tweet_job.minute.every(30)

# Set scrap jobs daily
scrap_job = cron.new("python jobs-under-280/core.py --scrap_job", comment="Scrap jobs from HN & AngelList")
scrap_job.day.every(1)

cron.write()