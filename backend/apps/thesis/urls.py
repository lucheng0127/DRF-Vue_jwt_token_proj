#-*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from apps.thesis.views import ThesisViewSet, ThesisMaterials, GetMaterial

router = routers.SimpleRouter()
router.register(r'thesis', ThesisViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^materials/$', ThesisMaterials.as_view(), name='materials'),
    url(r'^get_material/$', GetMaterial.as_view(), name='get_material'),
]
