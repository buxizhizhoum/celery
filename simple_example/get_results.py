#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A simple example to get result from celery backend
"""
import time
from tasks import sendmail
from tasks import add

if __name__ == "__main__":
    while True:
        # result = sendmail.delay("Einstein")
        result = add.delay(1, 2)

        while not result.ready():
            time.sleep(1)
        print("task done: %s" % result.get())
