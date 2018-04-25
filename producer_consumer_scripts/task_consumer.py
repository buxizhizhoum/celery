#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
start task_comsumer with celcey
"""
import random
import time
from celery import Celery


celery = Celery('task_consumer', broker='redis://localhost:6379/0')
celery.config_from_object('celery_config')  # read config from config file


@celery.task()
def task_consumers(number):
    print("consumer get number: %s" % number)
    time.sleep(1)
    print("consumer task done.")


@celery.task()
def add(x, y):
    print("Numbers to add is: %s, %s" % (x, y))
    res = x + y
    return res

