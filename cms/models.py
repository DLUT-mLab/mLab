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
    pub_date = models.DateTimeField(u'发布日期', auto_now=True)
    # cover_url = models.CharField(u'封面图链接', max_length=400, blank=True, null=True)
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

    TEACHER = "teacher"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTOR = "doctor"
    MEMBER_TYPE = (
        (TEACHER, u'指导教师'), 
        (BACHELOR, u'在读本科生'),
        (MASTER, u'在读硕士'),
        (DOCTOR, u'在读博士'),
    )

    class Meta:
        verbose_name = u'成员'
        verbose_name_plural = u'成员'

    name = models.CharField(u'姓名', max_length=50)
    member_type = models.CharField(u'类别', max_length=50, choices=MEMBER_TYPE, default=MASTER)
    start_date = models.DateField(u'入学时间', auto_now=False)
    intro = models.TextField(u'简介', blank=True, null=True)


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


class Attachment(models.Model):

    DATA = 'data'
    PROGRAM = 'program'
    FILE_TYPE = (
        (DATA, u'数据集'), 
        (PROGRAM, u'程序工具'),
    )

    class Meta:
        verbose_name = u'文件'
        verbose_name_plural = u'文件'
    name = models.CharField('名称', max_length=200)
    file_type = models.CharField('文件类型', max_length=50, choices=FILE_TYPE, default=DATA)
    intro = models.TextField(u'简介', blank=True, null=True)
    content = models.FileField(u'内容', upload_to='uploads/')


    def __unicode__(self):
        return self.name





