#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
start task_consumer with celery and feed data to celery with task_producer.py,
celery will process the task of task_producer.
"""
import random
import time
from task_consumer import task_consumers
from task_consumer import add


def task_producers():
    number = random.randint(1, 10)
    # result = task_consumer.delay(number)
    result = add.delay(number, number)
    while not result.ready():
        time.sleep(1)
    print("task result is ready")


if __name__ == "__main__":
    for i in range(10):
        task_producers()


# todo:
# task_producers with celery
