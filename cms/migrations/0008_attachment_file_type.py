# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20160307_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='file_type',
            field=models.CharField(choices=[('data', '\u6570\u636e\u96c6'), ('program', '\u7a0b\u5e8f\u5de5\u5177')], default='data', max_length=50, verbose_name='\u6587\u4ef6\u7c7b\u578b'),
        ),
    ]
