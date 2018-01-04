#-*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^', include('apps.user_info.urls')),
    url(r'^', include('apps.authx.urls')),
    url(r'^', include('apps.thesis.urls')),
    url(r'^', include('apps.notify.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])
