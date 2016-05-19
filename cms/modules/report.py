#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Article
from django.http import Http404
from utils.pagination import Pagination, PAGE_LIMIT


class HomeView(LayoutMixin, TemplateView):
    template_name="report/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        start = self.request.GET.get('start', 1)
        start = int(start) - 1 if int(start) - 1 >= 0 else 0
        context['latest_report'] = Article.objects\
                                          .filter(category__name=u'学术报告')\
                                          .order_by('pub_date')\
                                          .reverse()[start: start + PAGE_LIMIT]
        context['popular_report'] = Article.objects.filter(category__name=u'学术报告').order_by('read_count').reverse()
        all_count = Article.objects.filter(category__name=u'学术报告').count()
        context['pg'] = Pagination(start + 1, start + len(context['latest_report']), all_count)
        return context


class DetailView(LayoutMixin, TemplateView):
    template_name="report/detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            article = Article.objects.get(id=self.kwargs['article_id'])
        except Article.DoesNotExist:
            raise Http404
        article.read_count = article.read_count + 1
        article.save()
        context['article'] = article
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
