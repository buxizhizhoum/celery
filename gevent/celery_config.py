#!/usr/bin/python
# -*- coding: utf-8 -*-


# from __future__ import absolute_import, unicode_literals
# import os
# import sys
# sys.path.insert(0, os.getcwd())
#
# # ## Note: Start worker with -P gevent,
# # do not use the worker_pool option.
#
# broker_url = 'amqp://guest:guest@localhost:5672//'
# result_backend = 'amqp'
# result_expires = 30 * 60
#
# imports = ('tasks',)


from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_IMPORTS = ['gevent_tasks']
# CELERY_DEFAULT_QUEUE = 'pc'  # separate different celery instance
CELERY_ROUTES = {
    'gevent_tasks.calculate': {'queue': 'queue_cal'},
    'gevent_tasks.urlopen': {'queue': 'queue_url'},
}
# CELERYBEAT_SCHEDULE = {
#         "every-1-minute": {
#             # 'task': 'tasks.sendmail',
#             # 'task': 'tasks.add',
#             # 'task': 'producer_consumer.task_consumers',
#             # 'schedule': crontab(minute='*/1'),
#             'args': ("test_user")
#         }
# }
