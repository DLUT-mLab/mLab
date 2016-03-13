#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from .views import HomeView, MemberView


class Member(Module):
    order = 5
    icon = "mdi-action-account-child"

    @property
    def label(self):
        return u"成员介绍"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name='index'),
            url(r'^(?P<member_id>[0-9]+)/$', MemberView.as_view(), name='member'),
        ]

