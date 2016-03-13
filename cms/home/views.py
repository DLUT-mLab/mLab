#! coding=utf8
from django.views.generic import TemplateView
from material import LayoutMixin
from cms import models


class HomeView(LayoutMixin, TemplateView):
    title = "New Shipment"
    template_name="home/index.html"
    haha = "find you"
    