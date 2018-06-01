#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
relay on a class to hand mysql connections

could add mysql pool in the future
"""
import json
import time

from celery import Celery
from gevent_example.tools.mysqlwrapper import MySQLHandler

celery = Celery('gevent_mysql')
celery.config_from_object('celery_config')


class MySQLProcessor(object):
    def __init__(self, cfg, section):
        self.mysql = MySQLHandler(cfg, section)

    def read(self, company_id):
        sql = "select * from company where id = %d;" % company_id
        print(sql)
        tmp = self.mysql.execute_SQL(sql)
        res = tmp if tmp else None
        return res


mysql_processor = MySQLProcessor("./config/database.ini", "mysql:test")
# res = mysql_processor.read(1)
# print(res)


# @celery.task(ignore_result=True)
@celery.task(ignore_result=False)
def database_reader(company_id):
    print('company_id: {0}'.format(company_id))
    res = mysql_processor.read(company_id)
    time.sleep(10)
    return res


def read(company_id):
    res = database_reader.delay(company_id)
    while not res.ready():
        print("sleeping...")
        time.sleep(1)
    print("res: {}".format(res))
    return res


def read_json(json_string):
    company_id = json.loads(json_string)["company_id"]
    res = database_reader.delay(company_id)
    while not res.ready():
        print("sleeping...")
        time.sleep(1)
    print("res: {}".format(res))
    return res


if __name__ == "__main__":
    a = {"company_id": 1}
    b = json.dumps(a)
    read_json(b)
