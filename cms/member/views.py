#! coding=utf8
from django.views.generic import TemplateView
from material import LayoutMixin
from cms.models import Member
from django.shortcuts import render


class HomeView(LayoutMixin, TemplateView):
    title = "成员介绍"
    template_name="member/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['member_teacher'] = Member.objects.filter(member_type=Member.TEACHER)
        context['member_master'] = Member.objects.filter(member_type=Member.MASTER)
        context['member_doctor'] = Member.objects.filter(member_type=Member.DOCTOR)
        return context


class MemberView(LayoutMixin, TemplateView):
    title = "成员"
    template_name="member/member.html"

    def get_context_data(self, **kwargs):
        print self.kwargs['member_id']
        context = super(MemberView, self).get_context_data(**kwargs)
        context['member'] = Member.objects.get(id=self.kwargs['member_id'])
        return context