# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField(blank=True, null=True)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='cover_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Member'),
        ),
    ]