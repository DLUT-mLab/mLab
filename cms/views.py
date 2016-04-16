#! coding=utf8

from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def tasklog(request):
    m = {}
    task_id = request.POST.get('task_id', '')
    result = AsyncResult(task_id)
    m['state'] = result.state
    logfile = settings.MEDIA_ROOT + "/tasks/" + task_id + '/log.txt'
    try:
        with open(logfile, 'r') as f:
            m['logtext'] = f.read()
    except EnvironmentError:
        m['logtext'] = 'log is generating...'
    if result.state == "SUCCESS":
        try:
            with open(settings.MEDIA_ROOT + "/tasks/" + task_id + '/result.txt', 'r') as f:
                m['result'] = f.read()
        except EnvironmentError:
            m['result'] = 'Can not open result file'
    else:
        m['result'] = 'result is pending...'
    return HttpResponse(json.dumps(m))


