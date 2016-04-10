#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger
import os
from mlab import settings


logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def ppimirfs(filein, wppin):
    executable = os.path.join(settings.BASE_DIR, 'bin/PPImiRFS')
    pipe = os.popen('%s -i %s -p %s -o /tmp/result.txt' % (executable, filein, wppin), 'r')
    while True:
        line = pipe.readline()
        if not line:
            break
        logger.info(line)
