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


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    pass

    
@admin.register(Member)
class MemberAdmin(RichEditorModelAdmin):
    list_display = ('name', 'member_type', 'start_date')
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Attachment)
class AttachmentAdmin(RichEditorModelAdmin):
    list_display = ('file_type', 'name', 'intro', 'content')
    pass


