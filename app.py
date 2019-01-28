#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
this is used to work with ./application project
send task to celery and get result
"""
import time
import sys

# sys.path.append("./")
from application import tasks


if __name__ == "__main__":
    result1 = tasks.add.delay(1, 9)
    result2 = tasks.multiply.delay(1, 9)

    print("send task complete")

    while not result1.ready():
        time.sleep(1)
    #
    print(result1.get())

    while not result2.ready():
        time.sleep(1)

    print(result2.get())




