# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import AddUrls, Cases, CaseSuites, Login1
from .models import Login, Ym, Case, Case_suite
from rest_framework import generics, filters, viewsets, mixins
import requests
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
import re


# Create your views here.
# 新增域名
class AddUrl1(generics.ListCreateAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)


# 用户注册
class Register(generics.ListCreateAPIView):
    serializer_class = Login1
    queryset = Login.objects.filter(isdelete=False)

    def create(self, request, *args, **kwargs):
        data = request.data
        # hash = hashlib.sha1()
        try:
            # 创建用户信息
            Login.objects.create_user(username=data['username'],
                                      password=data['password'],
                                      email=data['email'])
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.exception(e)
            return Response(e)


# 查询所有域名信息
class UrlList(generics.ListAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)


# 搜索域名、项目名
class SearchUrl(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls
    filter_backends = (filters.SearchFilter,)
    search_fields = ('project_name', 'url_name')


# 更新域名
class UpdateUrl(generics.RetrieveUpdateAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)


# 删除域名
class DeleteUrl(generics.RetrieveDestroyAPIView):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def perform_destroy(self, instance):
        Ym.objects.filter(ym_id=instance.ym_id).update(isdelete=True)


# 批量删除域名
class DeleteUrls(APIView):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def put(self, request):

        data = request.data
        for i in data["ids"]:
            try:
                Ym.objects.filter(ym_id=i).update(isdelete=True)
                return Response("{'code': 200, 'message': '成功'}")

            except Exception as e:
                logging.exception(e)
                return Response(e)


# 新增测试用例
class AddCase(generics.ListCreateAPIView):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases


# 查询测试用例列表
class CaseList(generics.ListAPIView):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases


# 更新测试用例信息
class UpdateCase(generics.RetrieveUpdateAPIView):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases


# 搜索测试用例信息
class SearchCase(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'url', 'case_name', 'request_type', 'project_name__project_name')


# 删除测试用例
class DeleteCase(generics.RetrieveDestroyAPIView):
    queryset = Case.objects.all().filter(isdelete=False)
    serializer_class = Cases

    def perform_destroy(self, instance):
        Case.objects.filter(case_id=instance.case_id).update(isdelete=True)


# 增加测试套件
class AddCaseSuite(generics.ListCreateAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites


# 查询测试套件列表
class CaseSuiteList(generics.ListAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites


# 搜索测试套件
class SearchSuite(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
    filter_backends = (filters.SearchFilter,)
    search_fields = ('suite_name', 'project_name__project_name', 'status')


# 更新测试用例套件
class UpdateCaseSuite(generics.RetrieveUpdateAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites


# 删除测试套件
class DeleteCaseSuite(generics.RetrieveDestroyAPIView):
    queryset = Case_suite.objects.all().filter(isdelete=False)
    serializer_class = CaseSuites

    def perform_destroy(self, instance):
        Case_suite.objects.filter(suite_id=instance.suite_id).update(
            isdelete=True)


# 运行单接口套件
class Quest(APIView):

    def get_case(self):
        # 查询要运行的套件信息
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            t = requests.get(url, json=request_data, headers=headers,
                             verify=False)
            if t.status_code == 200:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())

                return Response(t.json(), status=status.HTTP_200_OK,
                                headers=headers)
                # return Response(t)
            else:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='失败')
                return Response(t.json(), status=t.status_code,
                                headers=headers)
        except Exception as e:
            return Response(e)

    def post_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            t = requests.post(url, json=eval(request_data),
                              headers=headers, verify=False)
            if t.status_code == 201:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())
                return Response(t.json(),
                                status=status.HTTP_201_CREATED,
                                headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='失败')
                return Response(t.json(), status=t.status_code,
                                headers=headers)
        except Exception as e:
            return Response(e)

    def put_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            t = requests.put(url, json=eval(request_data),
                             headers=headers, verify=False)
            if t.status_code == 200:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())
                return Response(t.json(), status=status.HTTP_200_OK,
                                headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='失败')
                return Response(t.json(), status=t.status_code,
                                headers=headers)
        except Exception as e:
            return Response(e)

    def delete_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            t = requests.delete(url, json=eval(request_data),
                                headers=headers, verify=False)
            if t.status_code == 204:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='成功')
                return Response(t.json(),
                                status=status.HTTP_204_NO_CONTENT,
                                headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=serializers['suite_id']).update(
                    status='失败')
                return Response(t.json(), status=t.status_code,
                                headers=headers)
        except Exception as e:
            return Response(e)

    def post(self, request):
        # 获取前端提交的数据
        global serializers
        serializers = request.data
        # 查询要运行的套件信息
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # # 获取请求地址
            url = data.yuming.url_name + data1.url
            # # 获取请求数据
            request_data = data1.request_data
            # # 获取请求类型
            request_type = data1.request_type
            # # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type": "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            # 请求参数未填写情况下赋值空值
            # if request_data == '':
            #     request_data = {}
            # get请求处理
            logging.debug('不调用其他接口返回数据')
            if data1.case_bz == "":
                if request_type == 'get':
                    results = self.get_case()
                    return Response(results.data)
                # post请求处理
                if request_type == 'post':
                    results = self.post_case()
                    return Response(results.data)
                # put请求处理
                if request_type == 'put':
                    results = self.put_case()
                    return Response(results.data)
                # delete请求处理
                if request_type == 'delete':
                    results = self.delete_case()
                    return Response(results.data)
            if data1.case_bz != "":
                for i in eval(data1.case_bz):
                    try:
                        # 通过正则找到要替换的字段，进行替换
                        res = re.compile('(\[\w*_?\w*\])')
                        # 查找到带【】的参数
                        t1 = res.search(url)
                        body_res = res.findall(request_data)
                        if t1 and len(body_res) > 0:
                            # 将【】替换为空
                            t1 = t1.group(0)
                            t2 = t1.replace('[', '')
                            t2 = t2.replace(']', '')
                            url_pattern = (
                                eval(Case.objects.get(case_id=i).result)[
                                    t2])
                            new_body = ''
                            for i in body_res:
                                new_body = request_data.replace(i, str(
                                    url_pattern))
                            # 查询上一个接口返回的数据，替换url中的参数

                            new_url = url.replace(t1, str(url_pattern))
                            if request_type == 'put':
                                t = requests.put(new_url,
                                                 json=eval(new_body),
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(isdelete=False,
                                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'post':
                                t = requests.post(new_url,
                                                  json=eval(new_body),
                                                  headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'get':
                                t = requests.get(new_url,
                                                 json=new_body,
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)

                            if request_type == 'delete':
                                t = requests.delete(new_url,
                                                    json=new_body,
                                                    headers=headers)
                                if t.status_code == 204:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update()
                                    return Response(
                                        status=status.HTTP_204_NO_CONTENT,
                                        headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(
                                        status=t.status_code,
                                        headers=headers)
                        elif t1 and len(body_res) == 0:
                            t1 = t1.group(0)
                            t2 = t1.replace('[', '')
                            t2 = t2.replace(']', '')
                            url_pattern = (
                                eval(Case.objects.get(case_id=i).result)[
                                    t2])
                            # 查询上一个接口返回的数据，替换url中的参数

                            new_url = url.replace(t1, str(url_pattern))
                            if request_type == 'put':
                                t = requests.put(new_url,
                                                 json=eval(request_data),
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(isdelete=False,
                                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'post':
                                t = requests.post(new_url,
                                                  json=eval(request_data),
                                                  headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'get':
                                t = requests.get(new_url,
                                                 json=request_data,
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)

                            if request_type == 'delete':
                                t = requests.delete(new_url,
                                                    json=request_data,
                                                    headers=headers)
                                if t.status_code == 204:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update()
                                    return Response(
                                        status=status.HTTP_204_NO_CONTENT,
                                        headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(
                                        status=t.status_code,
                                        headers=headers)
                        if not t1 and len(body_res) > 0:
                            # 将【】替换为空
                            new_data = request_data
                            for body in body_res:
                                print(body_res)
                                new_body = body.replace('[', '')
                                new_body = str(new_body).replace(']', '')
                                new_body = eval(
                                    Case.objects.get(case_id=i).result)[
                                    new_body]
                                new_data = new_data.replace(body,
                                                                '\'' + str(
                                                                    new_body) + '\'')
                                print(new_data)
                            # 查询上一个接口返回的数据，替换url中的参数
                            if request_type == 'put':
                                t = requests.put(url,
                                                 json=eval(new_data),
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(isdelete=False,
                                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'post':
                                t = requests.post(url,
                                                  json=eval(new_data),
                                                  headers=headers)
                                if t.status_code == 201:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)
                            if request_type == 'get':
                                t = requests.get(url,
                                                 json=new_data,
                                                 headers=headers)
                                if t.status_code == 200:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update(
                                        result=t.json())
                                    return Response(t.json(),
                                                    status=status.HTTP_200_OK,
                                                    headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(t.json(),
                                                    status=t.status_code,
                                                    headers=headers)

                            if request_type == 'delete':
                                t = requests.delete(url,
                                                    json=new_data,
                                                    headers=headers)
                                if t.status_code == 204:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='成功')
                                    Case.objects.filter(
                                        isdelete=False,
                                        case_name=data.case.case_name).update()
                                    return Response(
                                        status=status.HTTP_204_NO_CONTENT,
                                        headers=headers)
                                else:
                                    Case_suite.objects.filter(
                                        suite_id=serializers[
                                            'suite_id']).update(
                                        status='失败')
                                    return Response(
                                        status=t.status_code,
                                        headers=headers)
                    except Exception as e:
                        return Response(e)

        except Exception as e:
            return Response(e)


# 运行多个接口
class RunCaseSuites(APIView):
    def post(self, request):
        serializers = request.data
        # 循环获取到的接口列表
        for i in serializers["ids"]:
            # 获取运行的套件
            data = Case_suite.objects.get(suite_id=i)
            # 获取套件下的测试用例
            data1 = Case.objects.filter(isdelete=False).get(
                case_name=data.case.case_name)
            try:
                # 获取headers
                headers = data.headers
                headers = eval(headers)
                # 获取请求地址
                url = data.yuming.url_name + data1.url
                # 获取请求数据
                request_data = data1.request_data
                # 获取请求类型
                request_type = data1.request_type
                # 获取token
                token = requests.post("http://127.0.0.1:8000/api-auth/",
                                      json={"username": "zhengxq1",
                                            "password": "zxq111111"},
                                      headers={
                                          "Content-Type": "application/json; charset=utf-8"})
                headers["Authorization"] = "Jwt " + token.json()['token']
                # 请求参数为空，赋值空字典
                if request_data == '':
                    request_data = {}
                # get请求处理
                if request_type == 'get':
                    t = requests.get(url, json=request_data, headers=headers,
                                     verify=False)
                    if t.status_code == 200:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='成功')
                        return Response(t.json(), status=status.HTTP_200_OK,
                                        headers=headers)
                    else:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='失败')
                        return Response(t.json(), status=t.status_code,
                                        headers=headers)
                # post请求处理
                if request_type == 'post':
                    t = requests.post(url, json=eval(request_data),
                                      headers=headers, verify=False)
                    if t.status_code == 200:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='成功')
                        return Response(t.json(),
                                        status=status.HTTP_201_CREATED,
                                        headers=headers)
                    else:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='失败')
                        return Response(t.json(), status=t.status_code,
                                        headers=headers)
                # put请求处理
                if request_type == 'put':
                    t = requests.put(url, json=eval(request_data),
                                     headers=headers)
                    if t.status_code == 200:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='成功')
                        return Response(t.json(), status=status.HTTP_200_OK,
                                        headers=headers, verify=False)
                    else:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='失败')
                        return Response(t.json(), status=t.status_code,
                                        headers=headers)
                # delete请求处理
                if request_type == 'delete':
                    t = requests.delete(url, json=eval(request_data),
                                        headers=headers, verify=False)
                    if t.status_code == 204:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='成功')
                        return Response(t.json(), status=status.HTTP_200_OK,
                                        headers=headers)
                    else:
                        Case_suite.objects.filter(suite_id=i).update(
                            status='失败')
                        return Response(t.json(), status=t.status_code,
                                        headers=headers)
            except Exception as e:
                return Response(e)


# 搜索用户名、邮箱
class SearchUser(mixins.ListModelMixin, viewsets.GenericViewSet):
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


# 批量删除测试用例
class DeleteCases(APIView):
    queryset = Case.objects.all().filter(isdelete=False)
    serializer_class = Cases

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}
        error_message = {"code": 0, 'message': '用例已被删除'}
        list1 = []

        data = request.data
        for i in data["ids"]:
            try:
                Case.objects.filter(case_id=i).update(isdelete=True)

            except Exception as e:
                logging.exception(e)
        return Response(return_message)


# 批量删除测试套件
class DeleteCaseSuites(APIView):
    queryset = Case_suite.objects.all().filter(isdelete=False)
    serializer_class = CaseSuites

    def put(self, request):
        t = {'code': 200, 'message': '成功'}
        data = request.data
        for i in data["ids"]:
            try:
                Case_suite.objects.filter(suite_id=i).update(isdelete=True)
            except Exception as e:
                logging.exception(e)
        return Response(t)


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
