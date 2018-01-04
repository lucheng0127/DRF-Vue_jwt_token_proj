#-*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.notify.models import Notify
from apps.notify.serializers import NotifySerializer
from apps.notify.permissions import IsDirectorOrReadOnly


class NotifyViewSet(viewsets.ModelViewSet):
    serializer_class = NotifySerializer
    queryset = Notify.objects.all()
    permission_classes = (IsAuthenticated, IsDirectorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
