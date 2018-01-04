# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from apps.notify.views import NotifyViewSet

router = routers.SimpleRouter()
router.register('notify', NotifyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
