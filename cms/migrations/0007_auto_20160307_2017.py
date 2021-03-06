# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20160305_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='\u7b80\u4ecb')),
                ('content', models.FileField(upload_to='uploads/', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6',
                'verbose_name_plural': '\u6587\u4ef6',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='cover_url',
        ),
    ]
