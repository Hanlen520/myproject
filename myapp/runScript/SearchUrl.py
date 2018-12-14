# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from myapp.models import Ym
from rest_framework import filters, viewsets, mixins


# 搜索域名、项目名
class SearchUrl(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_name', 'url_name')
