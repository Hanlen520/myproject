"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import AddUrl1
from .views import SearchUrl, UpdateUrl, AddCase, AddCaseSuite, UrlList, DeleteUrl, CaseList, UpdateCase, DeleteCase, \
    SearchCase, CaseSuiteList, SearchSuite, UpdateCaseSuite, DeleteCaseSuite, Register, Quest, SearchUser, DeleteUser, \
    UpdateUser, ResetPwd, DeleteUrls, DeleteCases, DeleteCaseSuites, DeleteUsers, RunCaseSuites
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^api-auth/$', obtain_jwt_token, name='login'),
    url(r'^add_url/$', AddUrl1.as_view(), name='add_url'),
    url(r'^search_url/$', SearchUrl.as_view({'get': 'list'}), name='search_url'),
    url(r'^update_url/(?P<pk>\d+)/$', UpdateUrl.as_view(), name='update_url'),
    url(r'^add_cases/$', AddCase.as_view(), name='add_case'),
    url(r'^add_case_suite/$', AddCaseSuite.as_view(), name='add_case_suite'),
    url(r'^url_list/$', UrlList.as_view(), name='url_list'),
    url(r'^delete_url/(?P<pk>\d+)/$', DeleteUrl.as_view(), name='delete_url'),
    url(r'^case_list/$', CaseList.as_view(), name='case_list'),
    url(r'^update_case/(?P<pk>\d+)/$', UpdateCase.as_view(), name='update_case'),
    url(r'^delete_case/(?P<pk>\d+)/$', DeleteCase.as_view(), name='delete_case'),
    url(r'^search_case/$', SearchCase.as_view({'get': 'list'}), name='search_case'),
    url(r'^case_suite_list/$', CaseSuiteList.as_view(), name='case_suite_list'),
    url(r'^search_suite/$', SearchSuite.as_view({'get': 'list'}), name="search_suite"),
    url(r'^update_case_suite/(?P<pk>\d+)/$', UpdateCaseSuite.as_view(), name="update_case_suite"),
    url(r'^delete_case_suite/(?P<pk>\d+)/$', DeleteCaseSuite.as_view(), name='delete_case_suite'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^run/$', Quest.as_view(), name='quest'),
    url(r'^user_list/$', Register.as_view(), name='user_list'),
    url(r'^add_user/$', Register.as_view(), name='add_user'),
    url(r'^search_user/$', SearchUser.as_view({'get': 'list'}), name='search_user'),
    url(r'^delete_user/(?P<pk>\d+)/$', DeleteUser.as_view(), name="delete_user"),
    url(r'^update_user/(?P<pk>\d+)/$', UpdateUser.as_view(), name="update_user"),
    url(r'^reset_pwd/(?P<pk>\d+)/$', ResetPwd.as_view(), name="reset_pwd"),
    url(r'^delete_urls/$', DeleteUrls.as_view(), name='delete_urls'),
    url(r'^delete_cases/$', DeleteCases.as_view(), name='delete_cases'),
    url(r'^delete_case_suites/$', DeleteCaseSuites.as_view(), name='delete_case_suites'),
    url(r'^delete_users/$', DeleteUsers.as_view(), name='delete_users'),
    url(r'^run_case_suites/$', RunCaseSuites.as_view(), name='run__case_suites')

]
