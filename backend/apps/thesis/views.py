#-*- coding: utf-8 -*-

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.thesis.models import Thesis
from apps.thesis.serializers import ThesisSerializer
from apps.thesis.permissions import IsOwnerOrReadOnly


class ThesisViewSet(viewsets.ModelViewSet):
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        if self.request.user.user_info.role == 'admin' or self.request.user.user_info.role == 'college_leader':
            return Thesis.objects.all()
        elif self.request.user.user_info.role == 'subject_leader':
            try:
                dep = self.request.user.user_info.job.split('_',)[0]
                return Thesis.objects.filter(Q(stu_subj=dep) | Q(instructor=self.request.user))
            except Exception as e:
                return self.request.user.thesis.all()
        return self.request.user.thesis.all()

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

