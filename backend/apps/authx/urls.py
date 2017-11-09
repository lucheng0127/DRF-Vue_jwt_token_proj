#-*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from apps.authx.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
