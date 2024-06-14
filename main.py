# -*- encoding: UTF-8 -*-

import utils
import logging
import work_flow
import settings
import schedule
import time
import datetime
from pathlib import Path


def job():
    if utils.is_weekday():
        work_flow.prepare()

log_name = datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')

logging.basicConfig(format='%(asctime)s %(message)s', filename=f'sequoia_{log_name}.log')
logging.getLogger().setLevel(logging.INFO)
settings.init()

if settings.config['cron']:
    EXEC_TIME = "15:15"
    schedule.every().day.at(EXEC_TIME).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    work_flow.prepare()
