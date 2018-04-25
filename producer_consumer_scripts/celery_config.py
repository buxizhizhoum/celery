#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
config file of celery
"""
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERYBEAT_SCHEDULE={
        "every-1-minute": {
            'task': 'task_consumer.task_consumers',
            'schedule': crontab(minute='*/1'),
            'args': ("test_user")
        }
}
