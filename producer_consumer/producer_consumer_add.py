#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
producer and consumer completed with celery

Usage:
    cd to the directory where the script to run is in.
    start celery:

        celery -A producer_consumer worker --loglevel=info

NOTICE
    The task name of celery in the same backend should not be the same,
    otherwise there will be competition of task and some tasks will fail
    for celery.backends.base.NotRegistered.

how to accelerate?
"""
import random
import time
from celery import Celery


# celery = Celery('producer_consumer')
celery = Celery('producer_consumer', broker='redis://localhost:6379/0',
                backend='redis://localhost:6379/0')
# this is another method to provide config info
# celery.config_from_object('celery_config')


def task_producers():
    """
    this function produce tasks,
    :return:
    """
    number = random.randint(1, 10)
    print("task distributed: %s." % number)
    result = add.delay(number, number)  # get result of the task
    while not result.ready():
        time.sleep(0.1)
    print("task result is: %s" % result.get())


@celery.task()
def add(x, y):
    print("Numbers to add is: %s, %s" % (x, y))
    res = x + y
    time.sleep(1)
    return res


if __name__ == "__main__":
    while True:
        task_producers()

