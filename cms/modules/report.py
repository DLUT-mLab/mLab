#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Article
from django.shortcuts import render


class HomeView(LayoutMixin, TemplateView):
    template_name="report/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['latest_report'] = Article.objects.filter(category__name=u'学术报告').order_by('pub_date').reverse()
        return context


class DetailView(LayoutMixin, TemplateView):
    template_name="report/detail.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['article_id']
        context = super(DetailView, self).get_context_data(**kwargs)
        context['report'] = Article.objects.get(id=self.kwargs['article_id'])
        return context


class ReportModule(Module):
    order = 5
    icon = "mdi-action-description"
    slug = 'report'

    @property
    def label(self):
        return u"学术报告"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<article_id>[0-9]+)/$', DetailView.as_view(), name='detail')

        ]

