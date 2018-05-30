#!/usr/bin/python
# -*- coding: utf-8 -*-

from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_IMPORTS = ['producer_consumer']
CELERY_DEFAULT_QUEUE = 'pc'  # separate different celery instance
# CELERY_ROUTES = {
#     'producer_consumer': {'queue': 'pc'},
# }
# CELERYBEAT_SCHEDULE = {
#         "every-1-minute": {
#             # 'task': 'tasks.sendmail',
#             # 'task': 'tasks.add',
#             # 'task': 'producer_consumer.task_consumers',
#             # 'schedule': crontab(minute='*/1'),
#             'args': ("test_user")
#         }
# }
