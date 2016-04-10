#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin, Layout
from django.views.generic.edit import FormView
from django import forms
from cms.tasks import ppimirfs


class HomeView(LayoutMixin, TemplateView):
    template_name = "platform/index.html"

    def get_context_data(self, **kargs):
        context = super(HomeView, self).get_context_data(**kargs)
        return context


class PPimiRFSForm(forms.Form):
    inputfile = forms.FileField(label="预测文件")
    wppinfile = forms.FileField(label="权重网络数据文件")

    layout = Layout('inputfile', 'wppinfile')

    def run_task(self):
        print "run task"


class PPImiRFSView(LayoutMixin, FormView):
    template_name="platform/ppimirfs.html"
    form_class = PPimiRFSForm
    success_url = '/platform/'

    def get_context_data(self, **kwargs):
        context = super(PPImiRFSView, self).get_context_data(**kwargs)
        context['article'] = 11
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.run_task()
        return super(PPImiRFSView, self).form_valid(form)


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
            url(r'^ppimirfs/$', PPImiRFSView.as_view(), name='ppimirfs')
        ]
