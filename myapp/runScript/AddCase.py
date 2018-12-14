# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework import generics


class AddCase(generics.ListCreateAPIView):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases
