#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from application import celery  # import from __init__.py


@celery.task()
def add(x, y):
    time.sleep(1)
    return x + y


@celery.task
def multiply(x, y):
    time.sleep(1)
    return x * y



