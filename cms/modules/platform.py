#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin, Layout
from django.views.generic.edit import FormView
from django import forms
from cms.tasks import ppimirfs
from django.contrib.auth.mixins import LoginRequiredMixin
from celery.result import AsyncResult
from django.http import HttpResponseRedirect


class HomeView(LayoutMixin, TemplateView):
    template_name = "platform/index.html"

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        return context


class PPimiRFSForm(forms.Form):
    inputfile = forms.FileField(label="predicted_miRNA_pairs.txt")
    wppinfile = forms.FileField(label="wppin.txt")

    layout = Layout('inputfile', 'wppinfile')

    def run_task(self, taskid):
        data = self.cleaned_data['inputfile']
        wppin = self.cleaned_data['wppinfile']

        res = ppimirfs.delay(data, wppin)
        return res.id


class PPImiRFSView(LayoutMixin, LoginRequiredMixin, FormView):
    template_name="platform/ppimirfs.html"
    form_class = PPimiRFSForm
    success_url = '/platform/result/'

    def get_context_data(self, **kwargs):
        context = super(PPImiRFSView, self).get_context_data(**kwargs)
        context['article'] = 11
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        tid = form.run_task(self.request.user.id)
        return HttpResponseRedirect('/platform/result/%s/' % tid)
        #  return super(PPImiRFSView, self).form_valid(form)


class ResultView(LayoutMixin, LoginRequiredMixin, TemplateView):
    template_name="platform/result.html"

    def get_context_data(self, **kwargs):
        task_id = self.kwargs['task_id']
        result = AsyncResult(task_id)
        context = super(ResultView, self).get_context_data(**kwargs)
        context['result'] = result
        return context


class PlatformModule(Module):
    order = 8
    icon = "mdi-file-cloud-done"
    slug = 'platform'

    @property
    def label(self):
        return u"在线预测平台"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^ppimirfs/$', PPImiRFSView.as_view(), name='ppimirfs'),
            url(r'^result/(?P<task_id>.+)/$', ResultView.as_view(), name='result'),
        ]
