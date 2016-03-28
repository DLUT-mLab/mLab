#! coding=utf8

from __future__ import unicode_literals

from django.db import models
import html2text
import re


# Create your models here.
class Article(models.Model):

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    title = models.CharField(u'标题', max_length=400)
    author = models.ForeignKey('Member', verbose_name=u'作者', null=True, on_delete=models.SET_NULL)  # when author deleted set null
    category = models.ForeignKey('Category', verbose_name=u'文章分类', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(u'发布日期', auto_now=True)
    # cover_url = models.CharField(u'封面图链接', max_length=400, blank=True, null=True)
    content = models.TextField(u'正文')

    read_count = models.IntegerField(u'阅读量', default=0, null=True)

    def __unicode__(self):
        return self.title + '--' + self.author.name

    @property
    def url(self):
        return '/report/%s/' % self.id if self.category.name==u'学术报告' else '/news/%s/' % self.id

    @property
    def short_content(self):
        return html2text.html2text(self.content)[:140]

    @property
    def cover_url(self):
        pattern = re.compile(r'<img.*?src="(.*?)"')
        match = pattern.search(self.content)
        if match:
            return match.group(1)
        return ''


class Category(models.Model):

    class Meta:
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'

    name = models.CharField(u'分类名称', max_length=50)
    url = models.CharField(u'分类链接', max_length=50)

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
    member_type = models.CharField(u'类别', max_length=50, choices=MEMBER_TYPE, default=MASTER, db_index=True)
    start_date = models.DateField(u'入学时间', auto_now=False)
    intro = models.TextField(u'简介', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def url(self):
        return '/member/%s/' % (self.id, )


class Project(models.Model):

    class Meta:
        verbose_name = u'项目或研究方向'
        verbose_name_plural = u'项目或研究方向'

    PROJECT = u'project'
    RESEARCH = u'research'
    TYPE = (
        (PROJECT, '科研项目'),
        (RESEARCH, '学术研究'),
    )

    name = models.CharField(u'名称', max_length=100)
    project_type = models.CharField(u'类型', max_length=50, choices=TYPE, default=PROJECT, db_index=True)
    intro = models.TextField(u'简介', blank=True, null=True)
    start_date = models.DateField(u'开始时间', null=False)
    end_date = models.DateField(u'结束时间', blank=True, null=True)
    members = models.ManyToManyField(
        'Member',
        verbose_name=u'成员',
        through='Membership',
        through_fields=('project', 'member'),
    )
    achievement = models.TextField(u'成果', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def ongoing(self):
        return len(self.end_date)==0

    @property
    def url(self):
        return '/project/%s/' % self.id if self.project_type == self.PROJECT else '/research/%s/' % self.id


class Membership(models.Model):

    class Meta:
        verbose_name = u'成员关系'
        verbose_name_plural = u'成员关系'

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.member.name + ' <---> ' + self.project.name


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
    file_type = models.CharField('文件类型', max_length=50, choices=FILE_TYPE, default=DATA, db_index=True)
    intro = models.TextField(u'简介', blank=True, null=True)
    content = models.FileField(u'内容', upload_to='uploads/')
    pub_date = models.DateTimeField(u'发布日期', auto_now=True)

    def __unicode__(self):
        return self.name
