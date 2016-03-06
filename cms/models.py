#! coding=utf8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    title = models.CharField(u'标题', max_length=400)
    author = models.ForeignKey('Member', verbose_name=u'作者', null=True, on_delete=models.SET_NULL)  #when author deleted set null 
    category = models.ForeignKey('Category', verbose_name=u'文章分类', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(u'发布日期')
    cover_url = models.CharField(u'封面图链接', max_length=400, blank=True, null=True)
    content = models.TextField(u'正文')

    def __unicode__(self):
        return self.title + '--' + self.author.name
    

class Category(models.Model):

    class Meta:
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'

    name = models.CharField(u'分类名称', max_length=50)

    def __unicode__(self):
        return self.name


class Member(models.Model):

    class Meta:
        verbose_name = u'成员'
        verbose_name_plural = u'成员'

    name = models.CharField(u'姓名', max_length=50)
    intro = models.TextField(u'简介', blank=True, null=True)
    is_teacher = models.BooleanField(u'是否指导老师', default=False)

    def __unicode__(self):
        return self.name


class Project(models.Model):

    class Meta:
        verbose_name = u'研究项目'
        verbose_name_plural = u'研究项目'

    name = models.CharField(u'项目名称', max_length=100)
    intro = models.TextField(u'项目介绍', blank=True, null=True)
    members = models.ManyToManyField(
        'Member',
        verbose_name=u'所有成员',
        through='Membership',
        through_fields=('project', 'member'),
    )

    def __unicode__(self):
        return self.name


class Membership(models.Model):

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

