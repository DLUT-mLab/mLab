#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Article

from django.http import Http404
from utils.pagination import Pagination, PAGE_LIMIT


class HomeView(LayoutMixin, TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        start = self.request.GET.get('start', 1)
        start = int(start) - 1 if int(start) - 1 >= 0 else 0
        context['latest_news'] = Article.objects\
                                        .filter(category__name=u'新闻动态')\
                                        .order_by('pub_date')\
                                        .reverse()[start: start + PAGE_LIMIT]
        context['popular_news'] = Article.objects.filter(category__name=u'新闻动态').order_by('read_count').reverse()[:10]
        all_count = Article.objects.filter(category__name=u'新闻动态').count()
        context['pg'] = Pagination(start + 1, start + len(context['latest_news']), all_count)
        return context


class DetailView(LayoutMixin, TemplateView):
    template_name="news/detail.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['article_id']
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            article = Article.objects.get(id=self.kwargs['article_id'])
        except Article.DoesNotExist:
            raise Http404
        article.read_count = article.read_count + 1
        article.save()
        context['article'] = article
        return context


class NewsModule(Module):
    order = 2
    icon = "mdi-action-assignment"
    slug = 'news'

    @property
    def label(self):
        return u"新闻动态"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<article_id>[0-9]+)/$', DetailView.as_view(), name='detail')
        ]
