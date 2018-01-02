"""a URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from accounts.views import home, about, contact, thanks


urlpatterns = [
    # 从django 1.10开始, 不再支持使用字符串来表示view函数
    path(r'^$', home, name='home'),
    path(r'^about/$', about, name='about'),
    path(r'^contact/$', contact, name='contact'),
    path(r'^thanks/$', thanks, name='thanks'),
    # 管理后台
    path(r'^admin/', admin.site.urls),

    # include
    path(r'^polls/', include('polls.urls')),
    path(r'^accounts/', include('accounts.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
