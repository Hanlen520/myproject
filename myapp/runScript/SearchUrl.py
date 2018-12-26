# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from myapp.models import Ym
from rest_framework import filters, viewsets, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 搜索域名、项目名
class SearchUrl(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_name', 'url_name')
