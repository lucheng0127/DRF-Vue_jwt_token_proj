#-*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from apps.user_info.views import UserInfoViewSet

router = routers.SimpleRouter()
router.register(r'user-info', UserInfoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
