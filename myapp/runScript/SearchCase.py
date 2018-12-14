# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework import filters, viewsets, mixins


# 搜索测试用例信息
class SearchCase(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'url', 'case_name', 'request_type', 'project_name__project_name')
