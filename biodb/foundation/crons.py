from django.core.management import call_command
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'foundation.my_cron_job'    # a unique code

    def do(self):
        print("Hello")

class ExtractAppleHealthkitData(CronJobBase):

    RUN_EVERY_MINS = 5# every 5 mins
    RETRY_AFTER_FAILURE_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'foundation.extract_apple_healthkit_data'

    def do(self):
        call_command('extract_data_from_xml')
