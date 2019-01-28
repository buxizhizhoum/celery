#!/usr/bin/python
# -*- coding: utf-8 -*-
from celery import Celery

# app = Celery("balabala)
# name could be anything, it influence name in tasks, @name.task()
celery = Celery("demo_application")
celery.config_from_object("application.celery_config")


