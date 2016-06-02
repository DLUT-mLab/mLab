#! coding=utf8

from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from cms.models import DownloadRequest
import json
from utils.mail import send_mail_download_request

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


def not_support(request):
    return render(request, 'common/not_support.html')


@csrf_exempt
def download_approve(request):
    m = {}
    m['code'] = 10001
    request_id = request.POST.get('request_id', '')
    approve = request.POST.get('approve', '0')
    if not request_id:
        m['msg'] = u'没有id'
    else:
        obj = DownloadRequest.objects.get(id=request_id)
        if not obj:
            m['msg'] = u'找不到申请'
        else:
            obj.approve = (approve == '1')
            obj.handle = True
            if send_mail_download_request(obj):
                m['code'] = 10000
                obj.save()
            else:
                m['msg'] = u'未知原因邮件发送失败'
    return HttpResponse(json.dumps(m))
