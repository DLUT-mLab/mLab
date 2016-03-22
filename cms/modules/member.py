#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Member
from django.shortcuts import render
from django.http import Http404



class HomeView(LayoutMixin, TemplateView):
    title = "成员介绍"
    template_name="member/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['member_teacher'] = Member.objects.filter(member_type=Member.TEACHER)
        context['member_master'] = Member.objects.filter(member_type=Member.MASTER).order_by('start_date')
        context['member_doctor'] = Member.objects.filter(member_type=Member.DOCTOR).order_by('start_date')
        return context


class MemberView(LayoutMixin, TemplateView):
    title = "成员"
    template_name="member/member.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['member_id']
        context = super(MemberView, self).get_context_data(**kwargs)
        try:
            context['member'] = Member.objects.get(id=self.kwargs['member_id'])
        except Member.DoesNotExist:
            raise Http404
        return context


class MemberModule(Module):
    order = 6
    icon = "mdi-action-account-child"
    slug = 'member'

    @property
    def label(self):
        return u"成员介绍"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<member_id>[0-9]+)/$', MemberView.as_view(), name='member'),
        ]

