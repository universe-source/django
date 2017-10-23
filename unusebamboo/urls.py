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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from accounts.views import home, about, contact, thanks


urlpatterns = [
    # 从django 1.10开始, 不再支持使用字符串来表示view函数
    url(regex=r'^$', view=home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^thanks/$', thanks, name='thanks'),
    # 管理后台
    url(r'^admin/', admin.site.urls),

    # include
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
