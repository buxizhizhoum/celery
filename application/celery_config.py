#!/usr/bin/python
# -*- coding: utf-8 -*-


BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TIMEZONE = "Asia/Shanghai"  # default is UTC

# application is the project name, it is necessary, otherwise, there will be
# KeyError, and NotRegistered Error
CELERY_IMPORTS = ['application.tasks']


