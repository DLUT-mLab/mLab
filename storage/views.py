#! coding=utf8
from django.shortcuts import render

# Create your views here.

from mlab.settings import BEANSDB_CLIENT
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from mlab import settings
from django.utils.http import urlencode
import urllib

@csrf_exempt
def wangEditor_file_upload(request):
    result = r"error|附件上传失败"
    if request.method == 'POST':
        file = request.FILES['wangEditorH5File']
        if not file:
            result = r"error|找不到文件"
        else:
            result = handle_uploaded_file(file)
    return HttpResponse(result)

def handle_uploaded_file(f):
    full_path = settings.MEDIA_ROOT + f.name
    with open(full_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    print 'handle ok'
    return urllib.quote(settings.MEDIA_URL + f.name)

