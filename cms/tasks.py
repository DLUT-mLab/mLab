#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import

from celery import shared_task
import os
from mlab import settings
import logging


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
def ppimirfs(filedata, filewppin):
    task_id = ppimirfs.request.id
    base_path = os.path.join(settings.MEDIA_ROOT, 'tasks/') + task_id

    try:
        os.mkdir(base_path)
    except:
        pass

    handler = logging.handlers.RotatingFileHandler(os.path.join(base_path, 'log.txt'))
    logger = logging.getLogger("ppimirfs")
    logger.addHandler(handler)
    logger.info('### Begin ' + task_id)

    data_path = os.path.join(base_path, 'data.txt')
    wppin_path = os.path.join(base_path, 'wppin.txt')
    result_path = os.path.join(base_path, 'result.txt')

    handle_uploaded_file(data_path, filedata)
    handle_uploaded_file(wppin_path, filewppin)

    executable = os.path.join(settings.BASE_DIR, 'bin')
    cmd = 'cd %s && ./PPImiRFS -i %s -p %s -o %s' % (executable, data_path, wppin_path, result_path)
    logger.info("Command:" + cmd)

    pipe = os.popen(cmd, 'r')
    while True:
        line = pipe.readline()
        if not line:
            break
        logger.info(line.rstrip())
    logger.info("### End " + task_id)


def handle_uploaded_file(name, f):
    with open(name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
