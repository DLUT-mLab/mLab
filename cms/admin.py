#! coding=utf8

from django.contrib import admin
from django.db import models
from django import forms
from .models import Article, Member, Project, Membership, Category, Attachment
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Register your models here.
class RichEditorModelAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_article_form.html'


@admin.register(Article)
class ArticleAdmin(RichEditorModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('title', 'author', 'category', 'pub_date')
    list_filter = ('category__name',)
    exclude = ['read_count', ]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    pass

    
class MemberShipInline(admin.TabularInline):
    model = Project.members.through
    verbose_name = u'参与成员'
    verbose_name_plural = u'参与成员'


@admin.register(Member)
class MemberAdmin(RichEditorModelAdmin):
    date_hierarchy = 'start_date'
    list_display = ('name', 'member_type', 'start_date')
    list_filter = ('member_type',)
    pass


@admin.register(Project)
class ProjectAdmin(RichEditorModelAdmin):
    date_hierarchy = 'start_date'
    list_filter = ('project_type',)
    list_display = ('name', 'project_type', 'start_date')
    filter_horizontal = ('members',)
    inlines = [ MemberShipInline, ]
    exclude = ['members',]
    pass


@admin.register(Attachment)
class AttachmentAdmin(RichEditorModelAdmin):
    list_display = ('file_type', 'name', 'intro', 'content', 'pub_date')
    pass


# @admin.register(Membership)
# class MemberShipAdmin(RichEditorModelAdmin):
#     pass




