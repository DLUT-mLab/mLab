#! coding=utf8

from django.contrib import admin
from .models import Article, Member, Project, Membership, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date')
    


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'is_teacher')
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass




