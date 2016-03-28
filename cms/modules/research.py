#! coding=utf8
from material.frontend import Module
from django.conf.urls import url


from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Project
from django.http import Http404


class HomeView(LayoutMixin, TemplateView):
    title = "hahhaha"
    template_name="research/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['research_ongoing'] = Project.objects.filter(project_type=Project.RESEARCH,
                                                             end_date__isnull=True).order_by('start_date').reverse()
        past_list = Project.objects.filter(project_type=Project.RESEARCH,
                                           end_date__isnull=False).order_by('end_date').reverse()
        """
        research_past_map = {}
        for i in past_list:
            key = i.end_date.format(u'Y年')
            if key not in research_past_map.keys():
                research_past_map[key] = []
            research_past_map[key].append(i)
        context['research_past_map'] = research_past_map
        """
        context['research_past'] = past_list
        return context


class DetailView(LayoutMixin, TemplateView):
    template_name="research/detail.html"

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
            url(r'^(?P<project_id>[0-9]+)/$', DetailView.as_view(), name='detail')
        ]
