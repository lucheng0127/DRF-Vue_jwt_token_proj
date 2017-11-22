#-*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.thesis.models import Thesis
from apps.thesis.serializers import ThesisSerializer


class ThesisViewSet(viewsets.ModelViewSet):
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.thesis.all()

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

