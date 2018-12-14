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
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from myapp.runScript import runCase, runCaseSuite, Login, AddUrls, Register, \
    UrlList, SearchUrl, UpdateUrl, DeleteUrl, DeleteUrls, AddCase, CaseList, \
    UpdateCase, SearchCase, DeleteCase, AddCaseSuite, CaseSuiteList, \
    SearchSuite, UpdateCaseSuite, DeleteCaseSuite, User, DeleteCases, \
    DeleteCaseSuites

urlpatterns = [
    url(r'^api-auth/$', obtain_jwt_token, name='login'),
    url(r'^add_url/$', AddUrls.AddUrl1.as_view(), name='add_url'),
    url(r'^search_url/$', SearchUrl.SearchUrl.as_view({'get': 'list'}),
        name='search_url'),
    url(r'^update_url/(?P<pk>\d+)/$', UpdateUrl.UpdateUrl.as_view(),
        name='update_url'),
    url(r'^add_cases/$', AddCase.AddCase.as_view(), name='add_case'),
    url(r'^add_case_suite/$', AddCaseSuite.AddCaseSuite.as_view(),
        name='add_case_suite'),
    url(r'^url_list/$', UrlList.UrlList.as_view(), name='url_list'),
    url(r'^delete_url/(?P<pk>\d+)/$', DeleteUrl.DeleteUrl.as_view(),
        name='delete_url'),
    url(r'^case_list/$', CaseList.CaseList.as_view(), name='case_list'),
    url(r'^update_case/(?P<pk>\d+)/$', UpdateCase.UpdateCase.as_view(),
        name='update_case'),
    url(r'^delete_case/(?P<pk>\d+)/$', DeleteCase.DeleteCase.as_view(),
        name='delete_case'),
    url(r'^search_case/$', SearchCase.SearchCase.as_view({'get': 'list'}),
        name='search_case'),
    url(r'^case_suite_list/$', CaseSuiteList.CaseSuiteList.as_view(),
        name='case_suite_list'),
    url(r'^search_suite/$', SearchSuite.SearchSuite.as_view({'get': 'list'}),
        name="search_suite"),
    url(r'^update_case_suite/(?P<pk>\d+)/$',
        UpdateCaseSuite.UpdateCaseSuite.as_view(),
        name="update_case_suite"),
    url(r'^delete_case_suite/(?P<pk>\d+)/$',
        DeleteCaseSuite.DeleteCaseSuite.as_view(),
        name='delete_case_suite'),
    url(r'^register/$', Register.Register1.as_view(), name='register'),
    url(r'^run/$', runCase.Quest.as_view(), name='quest'),
    url(r'^user_list/$', Register.Register1.as_view(), name='user_list'),
    url(r'^add_user/$', Register.Register1.as_view(), name='add_user'),
    url(r'^search_user/$', User.SearchUser.as_view({'get': 'list'}),
        name='search_user'),
    url(r'^delete_user/(?P<pk>\d+)/$', User.DeleteUser.as_view(),
        name="delete_user"),
    url(r'^update_user/(?P<pk>\d+)/$', User.UpdateUser.as_view(),
        name="update_user"),
    url(r'^reset_pwd/(?P<pk>\d+)/$', User.ResetPwd.as_view(), name="reset_pwd"),
    url(r'^delete_urls/$', DeleteUrls.DeleteUrls.as_view(), name='delete_urls'),
    url(r'^delete_cases/$', DeleteCases.DeleteCases.as_view(),
        name='delete_cases'),
    url(r'^delete_case_suites/$', DeleteCaseSuites.DeleteCaseSuites.as_view(),
        name='delete_case_suites'),
    url(r'^delete_users/$', User.DeleteUsers.as_view(), name='delete_users'),
    url(r'^run_case_suites/$', runCaseSuite.RunCaseSuites.as_view(),
        name='run__case_suites')

]
