# -*- coding:utf-8 -*-
from myapp.models import Case_suite
from myapp.serializers import CaseSuites
from rest_framework import mixins, filters, viewsets


# 搜索测试套件
class SearchSuite(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
    filter_backends = (filters.SearchFilter,)
    search_fields = ('suite_name', 'project_name__project_name', 'status')


