#! coding=utf8
from material.frontend import Module
from django.conf.urls import url


from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Project
from django.shortcuts import render


class HomeView(LayoutMixin, TemplateView):
    title = "hahhaha"
    template_name="research/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['research_ongoing'] = Project.objects.filter(project_type=Project.RESEARCH, ongoing=True)
        return context



class ResearchModule(Module):
    order = 3
    icon = "mdi-action-pageview"
    slug = 'research'

    @property
    def label(self):
        return u"学术研究"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
        ]