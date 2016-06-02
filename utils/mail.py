#! coding=utf8

from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException
import os


def send_mail_download_request(obj):
    result = False
    try:
        if obj.approve:
            url = settings.HOST + obj.file.content.url
            send_mail(
                subject=settings.EMAIL_SUBJECT_PREFIX + u'下载申请', 
                message=u'申请成功，下载地址是:' + url, 
                from_email=settings.SEND_MAIL_FROM, 
                recipient_list=[obj.email], 
                fail_silently=False)
        else:
            send_mail(
                subject=settings.EMAIL_SUBJECT_PREFIX + u'下载申请', 
                message=u'对不起，申请失败', 
                from_email=settings.SEND_MAIL_FROM, 
                recipient_list=[obj.email], 
                fail_silently=False)
        result = True
    except SMTPException, e:
        print e
    return result