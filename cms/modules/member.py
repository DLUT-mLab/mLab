#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms import models
from django.shortcuts import render


class HomeView(LayoutMixin, TemplateView):
    title = "成员介绍"
    template_name="member/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['member_teacher'] = models.Member.objects.filter(member_type=models.Member.TEACHER)
        context['member_master'] = models.Member.objects.filter(member_type=models.Member.MASTER).order_by('start_date')
        context['member_doctor'] = models.Member.objects.filter(member_type=models.Member.DOCTOR).order_by('start_date')
        return context


class MemberView(LayoutMixin, TemplateView):
    title = "成员"
    template_name="member/member.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['member_id']
        context = super(MemberView, self).get_context_data(**kwargs)
        context['member'] = Member.objects.get(id=self.kwargs['member_id'])
        return context


class Member(Module):
    order = 6
    icon = "mdi-action-account-child"

    @property
    def label(self):
        return u"成员介绍"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<member_id>[0-9]+)/$', MemberView.as_view(), name='member'),
        ]

