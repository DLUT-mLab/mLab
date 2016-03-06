#! coding=utf8

"""mlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import cms.views
from material.frontend import urls as frontend_urls
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'', include(frontend_urls)),
    url(r'^admin/', admin.site.urls),
    # url(r'^news/$', cms.views.news),
    # url(r'^acade/$', cms.views.acade),
    # url(r'^member/$', cms.views.member),
    # url(r'^album/$', cms.views.album),
    url(r'^summernote/', include('django_summernote.urls')),

]
