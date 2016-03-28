#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Article


class HomeView(LayoutMixin, TemplateView):
    template_name="home/index.html"

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        context['latest_news'] = Article.objects.filter(category__name=u'新闻动态').order_by('pub_date').reverse()[:10]
        context['latest_conference'] = Article.objects.filter(title__contains=u'会').order_by('pub_date').reverse()[:10]
        return context


class HomeModule(Module):
    order = 1
    icon = "mdi-action-account-balance"
    slug = 'home'

    @property
    def label(self):
        return u"首页"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name="index"),
        ]
