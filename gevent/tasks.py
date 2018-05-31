#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
celery -A <app_name> worker -c 3 -l INFO  # 启动3个worker，3个进程

celery -A <app_name> worker -l INFO -P gevent -c 1000  # 启动一个gevent worker，gevent并发数1000，只有一个进程

celery -A <app_name> multi start 2 -l INFO -P gevent -c 1000  -Q <queue_name>  # 启动2个gevent worker，每一个具有1000并发度，消费<queue_name>制定的队列

celery -A <app_name> multi start 4 -l INFO -P gevent -c:1-3 1000 -c:4 200 -Q:1-2 myQueue1 -Q:3 myQueue2 -Q:4 myQueue3  #　启动４个gevent worker，1-4具有1000并发度，4具有200并发度，1-2消费队列myQueue1, 3消费队列myQueue2，4消费队列myQueue3.
"""

from __future__ import absolute_import, print_function, unicode_literals
import time
import requests
from celery import Celery


celery = Celery('tasks', broker='redis://localhost:6379/0',
                backend='redis://localhost/0')


# @celery.task(ignore_result=True)
@celery.task(ignore_result=False)
def urlopen(url):
    print('Opening: {0}'.format(url))
    try:
        requests.get(url)
        time.sleep(1)
    except requests.exceptions.RequestException as exc:
        print('Exception for {0}: {1!r}'.format(url, exc))
        return url, 0
    print('Done with: {0}'.format(url))
    return url, 1


@celery.task()
def calculate(number):
    res = None
    for i in range(100):
        res = number ** number
    return res


def get_res(test_url):
    while True:
        res = urlopen.delay(test_url)
        print("url: {}".format(test_url))
        while not res.ready():
            time.sleep(0.1)
        print("result:{}".format(res.get()))


def get_cal_res(number):
    while True:
        res = calculate.delay(number)
        print("number: {}".format(number))
        while not res.ready():
            time.sleep(0.1)
        print("result:{}".format(res.get()))

if __name__ == "__main__":
    test_url = "https://www.baidu.com"
    # url_l = [test_url for i in range(10)]
    # map(get_res, url_l)
    # get_res(test_url)
    get_cal_res(100)
