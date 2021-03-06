# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20160415_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u59d3\u540d')),
                ('department', models.CharField(max_length=200, verbose_name='\u5de5\u4f5c\u5355\u4f4d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('apply_date', models.DateTimeField(auto_now=True, verbose_name='\u7533\u8bf7\u65e5\u671f')),
                ('approve', models.BooleanField(default=False, verbose_name='\u662f\u5426\u901a\u8fc7')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Attachment', verbose_name='\u4e0b\u8f7d\u6587\u4ef6')),
            ],
            options={
                'verbose_name': '\u4e0b\u8f7d\u7533\u8bf7',
                'verbose_name_plural': '\u4e0b\u8f7d\u7533\u8bf7',
            },
        ),
    ]
