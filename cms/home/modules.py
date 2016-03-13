#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from .views import HomeView

class Home(Module):
    order = 1
    icon = "mdi-action-account-balance"

    @property
    def label(self):
        return u"首页"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name="index"),
        ]

