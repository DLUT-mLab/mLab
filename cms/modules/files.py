#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Attachment
from django.http import Http404
from django.conf import settings
from django import forms
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect



class HomeView(LayoutMixin, TemplateView):
    title = "资料下载"
    template_name="files/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['dataset_list'] = Attachment.objects.filter(file_type=Attachment.DATA).order_by('pub_date').reverse()[:5]
        context['program_list'] = Attachment.objects.filter(file_type=Attachment.PROGRAM).order_by('pub_date').reverse()[:5]
        return context


class DatasetView(LayoutMixin, TemplateView):
    title = "数据集下载"
    template_name="files/dataset.html"

    def get_context_data(self, **kwargs):
        context = super(DatasetView, self).get_context_data(**kwargs)
        context['dataset_list'] = Attachment.objects.filter(file_type=Attachment.DATA).order_by('pub_date').reverse()[:5]
        return context


class ProgramView(LayoutMixin, TemplateView):
    title = "程序下载"
    template_name="files/program.html"

    def get_context_data(self, **kwargs):
        context = super(ProgramView, self).get_context_data(**kwargs)
        context['program_list'] = Attachment.objects.filter(file_type=Attachment.PROGRAM).order_by('pub_date').reverse()[:5]
        return context


class DownloadForm(forms.Form):

    name = forms.CharField(label=u'姓名')
    department = forms.CharField(label=u'工作单位')
    email = forms.EmailField(label=u'邮箱')
    agree = forms.BooleanField(label=u'是否同意协议')


class DetailView(LayoutMixin, FormView):
    title = "资料详情"
    template_name="files/detail.html"
    form_class = DownloadForm

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        try:
            context['file'] = Attachment.objects.get(id=self.kwargs['file_id'])
        except Attachment.DoesNotExist:
            raise Http404
        return context

    def form_valid(self, form):
        _id = self.kwargs['file_id']
        try:
            file = Attachment.objects.get(id=_id)
        except Attachment.DoesNotExist:
            raise Http404
        return HttpResponseRedirect(settings.MEDIA_URL + file.content.name)

    # def get_success_url(self):
    #     _id = self.get_form_kwargs()['data']['id']
    #     try:
    #         file = Attachment.objects.get(id=_id)
    #     except Attachment.DoesNotExist:
    #         raise Http404
    #     return settings.MEDIA_URL + file.content.name


class FilesModule(Module):
    order = 10
    icon = "mdi-action-work"
    slug = 'files'

    @property
    def label(self):
        return u"资料下载"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^dataset/', DatasetView.as_view(), name='dataset'),
            url(r'^program/', ProgramView.as_view(), name='program'),
            url(r'^(?P<file_id>[0-9]+)/$', DetailView.as_view(), name='detail'),
        ]
