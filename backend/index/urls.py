#-*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.user_info.urls')),
    url(r'^', include('apps.authx.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])
