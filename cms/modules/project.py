#! coding=utf8
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Project
from django.http import Http404

from material.frontend import Module


class HomeView(LayoutMixin, TemplateView):
    title = "hahhaha"
    template_name="project/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['project_ongoing'] = Project.objects.filter(project_type=Project.PROJECT,
                                                            end_date__isnull=True).order_by('start_date').reverse()
        past_list = Project.objects.filter(project_type=Project.PROJECT,
                                           end_date__isnull=False).order_by('end_date').reverse()
        context['project_past'] = past_list
        return context


class DetailView(LayoutMixin, TemplateView):
    template_name="project/detail.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['project_id']
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            project = Project.objects.get(id=self.kwargs['project_id'])
        except Project.DoesNotExist:
            raise Http404
        project.save()
        context['project'] = project
        return context


class ProjectModule(Module):
    order = 4
    icon = "mdi-action-work"
    slug = 'project'

    @property
    def label(self):
        return u'科研项目'

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<project_id>[0-9]+)/$', DetailView.as_view(), name='detail')

        ]
