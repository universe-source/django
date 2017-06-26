# coding:utf8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^login_error/$', views.login_error, name='login_error'),
    url(r'^main/$', views.main, name='main'),
]
