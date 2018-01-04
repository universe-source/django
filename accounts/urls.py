# coding:utf8
from django.urls import include, path, re_path
from . import views


app_name = 'accounts'
urlpatterns = [
    re_path(r'^login/$', views.login_user, name='login'),
    re_path(r'^logout/$', views.logout_user, name='logout'),
    re_path(r'^login_error/$', views.login_error, name='login_error'),
]
