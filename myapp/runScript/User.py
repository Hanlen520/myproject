# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Login1
from myapp.models import Login
from rest_framework import generics, filters, viewsets, mixins
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 搜索用户名、邮箱
class SearchUser(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Login.objects.filter(isdelete=False)
    serializer_class = Login1
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')


# 删除用户
class DeleteUser(generics.RetrieveDestroyAPIView):
    queryset = Login.objects.all().filter(isdelete=False)
    serializer_class = Login1

    def perform_destroy(self, instance):
        Login.objects.filter(user_id=instance.user_id).update(isdelete=True)


# 更新用户信息
class UpdateUser(generics.RetrieveUpdateAPIView):
    serializer_class = Login1
    queryset = Login.objects.filter(isdelete=False)


# 重置密码
class ResetPwd(generics.RetrieveUpdateAPIView):
    serializer_class = Login1
    queryset = Login.objects.filter(isdelete=False)

    def update(self, request, *args, **kwargs):
        data = request.data
        # hash = hashlib.sha1()
        try:
            # hash.update(bytes(data['password']))
            # password = hash.hexdigest()
            t = Login.objects.get(user_id=data['user_id'])
            t.set_password(data['password'])
            t.save()
        except Exception as e:
            logging.exception(e)
        return Response(data, status=status.HTTP_200_OK)


# 批量删除用户
class DeleteUsers(APIView):
    queryset = Login.objects.all().filter(isdelete=False)
    serializer_class = Login1

    def put(self, request):
        t = {'code': 200, 'message': '成功'}
        data = request.data
        for i in data["ids"]:
            try:
                Login.objects.filter(user_id=i).update(isdelete=True)
            except Exception as e:
                logging.exception(e)
        return Response(t)
