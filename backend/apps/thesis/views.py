#-*- coding: utf-8 -*-
import collections

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, list_route

from apps.thesis.models import Thesis, ThesisLog
from apps.thesis.serializers import ThesisSerializer, ThesisLogSerializer
from apps.thesis.permissions import IsOwnerOrReadOnly
from utils.validate import validator_text


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

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        lines = data.splitlines()
        good_data = []
        bad_data = []
        for line in lines:
            # 验证数据是否合理
            if len(line.split(',',)) != 5:
                bad_data.append(line)
                continue

            if not validator_text(line):
                bad_data.append(line)
                print(u'有特殊字符')
                continue

            cache_dic = {}
            cache_dic['stu_name'], cache_dic['stu_num'], \
            cache_dic['stu_subj'], cache_dic['graduation_year'], \
            cache_dic['title'] = line.split(',',)
            cache_dic['instructor'] = request.user
            # 判断该学生论文数据是否已经存在
            if Thesis.objects.filter(stu_num=cache_dic['stu_num']):
                bad_data.append(line)
                continue

            try:
                thesis = Thesis(**cache_dic)
                thesis.save()
                good_data.append(line)
            except Exception as e:
                bad_data.append(line)

        return Response({'success': len(good_data), 'failed': len(bad_data)}, status=status.HTTP_200_OK)

    @detail_route()
    def thesis_log(self, request, pk=None):
        thesis_log = self.get_object().thesis_log.all()
        serializer = ThesisLogSerializer(thesis_log, many=True)
        data = collections.OrderedDict()
        data['MANDATE'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "01任务书",
            "upload_times": 0
        }
        data['SCHEDULE1'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "02指导计划表(教师)",
            "upload_times": 0
        }
        data['SCHEDULE2'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "03指导计划表(学生)",
            "upload_times": 0
        }
        data['PROPOSAL'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "04开题报告",
            "upload_times": 0
        }
        data['CHECKLIST'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "05中期检查表",
            "upload_times": 0
        }
        data['PPT1'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "06中期检答辩PPT",
            "upload_times": 0
        }
        data['DEFENCE'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "07答辩申请表",
            "upload_times": 0
        }
        data['ADVICE'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "08导教师意见",
            "upload_times": 0
        }
        data['REVIEW'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "09评阅意见",
            "upload_times": 0
        }
        data['THESIS'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "10论文",
            "upload_times": 0
        }
        data['PPT2'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "11答辩PPT",
            "upload_times": 0
        }
        data['SCORE'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "12成绩登记表",
            "upload_times": 0
        }
        data['SOURCECODE'] = {
            "id": '',
            "last_upload_time": '',
            "filename_cn": "13源代码",
            "upload_times": 0
        }
        for item in serializer.data:
            if item.get('last_upload_time'):
                data[item.get('file')]['last_upload_time'] = item.get('last_upload_time')
            if item.get('id'):
                data[item.get('file')]['id'] = item.get('id')
            data[item.get('file')]['filename_cn'] = item.get('filename_cn')
            data[item.get('file')]['upload_times'] = item.get('upload_times')
        thesis_log_data = []
        for k, v in data.items():
            thesis_log_data.append(v)
        return Response({'data': thesis_log_data}, status=status.HTTP_200_OK)

    @detail_route()
    def top_5_log(self, request, pk=None):
        logs = self.get_object().thesis_log.all()
        if len(logs) <= 5:
            serializer = ThesisLogSerializer(logs, many=True)
        else:
            top_5_logs = logs[0:4]
            serializer = ThesisLogSerializer(top_5_logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)


class ThesisMaterials(APIView):
    '''
    get thesis materials choice
    '''
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        choices = []
        choices.append({
            'value': 'MANDATE',
            'filename': u'01任务书'
        })
        choices.append({
            'value': 'SCHEDULE1',
            'filename': u'02指导计划表(教师)'
        })
        choices.append({
            'value': 'SCHEDULE2',
            'filename': u'03指导计划表(学生)'
        })
        choices.append({
            'value': 'PROPOSAL',
            'filename': u'04开题报告'
        })
        choices.append({
            'value': 'CHECKLIST',
            'filename': u'05中期检查表'
        })
        choices.append({
            'value': 'PPT1',
            'filename': u'06中期检答辩PPT'
        })
        choices.append({
            'value': 'DEFENCE',
            'filename': u'07答辩申请表'
        })
        choices.append({
            'value': 'ADVICE',
            'filename': u'08导教师意见'
        })
        choices.append({
            'value': 'REVIEW',
            'filename': u'09评阅意见'
        })
        choices.append({
            'value': 'THESIS',
            'filename': u'10论文'
        })
        choices.append({
            'value': 'PPT2',
            'filename': u'11答辩PPT'
        })
        choices.append({
            'value': 'SCORE',
            'filename': u'12成绩登记表'
        })
        choices.append({
            'value': 'SOURCECODE',
            'filename': u'13源代码'
        })
        return Response(choices, status=status.HTTP_200_OK)
