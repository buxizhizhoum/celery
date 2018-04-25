#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A simple example of celery task


usage:
    cd to the directory where this script is in

    celery -A tasks worker --loglevel=info  # tasks is the name of this script

    python get_result.py to get the result from celery backend
"""
import time
from celery import Celery
# from celery.contrib import rdb

celery = Celery('tasks', broker='redis://localhost:6379/0',
                backend='redis://localhost/0')


# class MyTask(Celery.Task):
#     def on_success(self, retval, task_id, args, kwargs):
#         print('task done: {0}'.format(retval))
#         return super(MyTask, self).on_success(retval, task_id, args, kwargs)
#
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         print('task fail, reason: {0}'.format(exc))
#         return super(MyTask, self).on_failure(exc, task_id, args, kwargs,
#                                               einfo)


@celery.task()
def sendmail(mail):
    print('sending mail to %s...' % mail)
    time.sleep(2.0)
    print('mail sent.')
    return True


@celery.task()
def add(x, y):
    print("Numbers to add is: %s, %s" % (x, y))
    res = x + y
    # rdb.set_trace()
    return res


