#! coding=utf8

from django.contrib import admin
from django.db import models
from django import forms
from .models import Article, Member, Project, Membership, Category
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Register your models here.

class ArticleAdminForm(forms.ModelForm):
    # content = forms.CharField(widget=SummernoteInplaceWidget())
    class Meta:
        model = Article
        exclude = []
        # widgets = {
        #     # 'content': SummernoteWidget(),
        #     # 'content': SummernoteWidget(),
        # }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'pub_date'
    list_display = ('title', 'author', 'category', 'pub_date')
    change_form_template = 'admin/change_article_form.html'

    # form = ArticleAdminForm
    # formfield_overrides = {
    #     models.TextField: {'widget': SummernoteWidget},
    # }
    


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    pass

    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro', 'is_teacher')
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass




