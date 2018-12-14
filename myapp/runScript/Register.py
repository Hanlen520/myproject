# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Login1
from myapp.models import Login
from rest_framework import generics
import logging
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


# 用户注册
class Register1(generics.ListCreateAPIView):
    serializer_class = Login1
    queryset = Login.objects.filter(isdelete=False)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            # 创建用户信息
            Login.objects.create_user(username=data['username'],
                                      password=data['password'],
                                      email=data['email'])
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response(e)
