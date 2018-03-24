# coding:utf8
"""unusebamboo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



urlpatterns = [
    url(regex=r'^$', view='accounts.views.home', name='home'),
    url(r'^about/$', 'accounts.views.about', name='about'),
    url(r'^contact/$', 'accounts.views.contact', name='contact'),
    url(r'^thanks/$', 'accounts.views.thanks', name='thanks'),
    # 管理后台
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # 密码重置
    # 如果使用了kwargs参数：{'template_name': 'value'}，请确保自定义template的
    # 成功跳转
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.password_reset_complete, 
        name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
