#! coding=utf8
from material.frontend import Module
from django.conf.urls import url
from django.views.generic import TemplateView
from material import LayoutMixin
from cms import models


class HomeView(LayoutMixin, TemplateView):
    title = "New Shipment"
    template_name="home/index.html"
    haha = "find you"
    

class HomeModule(Module):
    order = 1
    icon = "mdi-action-account-balance"
    slug = 'home'

    @property
    def label(self):
        return u"首页"

    def get_urls(self):
        return [
            url(r'^$', HomeView.as_view(), name="index"),
        ]

