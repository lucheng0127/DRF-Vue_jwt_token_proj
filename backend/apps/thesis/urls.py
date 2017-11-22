#-*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from apps.thesis.views import ThesisViewSet

router = routers.SimpleRouter()
router.register(r'thesis', ThesisViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
