#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TIMEZONE = "Asia/Shanghai"  # default is UTC

# application is the project name, it is necessary, otherwise, there will be
# KeyError, and NotRegistered Error
CELERY_IMPORTS = ['application.tasks']

CELERYBEAT_SCHEDULE = {
        # set a name for the task
        "task_add": {
            'task': 'application.tasks.add',  # which task
            # run every one minute
            # 'schedule': crontab(minute='*/1'),  # one method

            # run every 10 seconds
            'schedule': datetime.timedelta(seconds=10),  # another method
            'args': (1, 2),
        },

        "task_mul": {
            "task": "application.tasks.multiply",
            # run at 19:28
            "schedule": crontab(hour=19, minute=28),
            "args": (1, 2),
        }

}


# start timing task
# celery beat -A <application_name> -l INFO

# start worker
# celery worker -A <application_name> -l INFO

# after starting timing task, worker should be started

# start celery beat and worker in one line
# celery -B -A <application_name>  worker -l INFO


