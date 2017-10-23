"""
Django settings for unusebamboo project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '29e3ohmh+=s^udbct$yg^2p+9n+fpdpp%+9-^or(g+o%@2oosm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin', # always before django.contrib.admin
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Static静态文件步骤1: 
    'django.contrib.staticfiles',

    'accounts',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'unusebamboo.urls'

# 配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 将模板存储在文件中, 而不是底层Template API, 保存模板的目录称为模板目录
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            # 上下文处理器: 自动传递一些上下文变量, 例如user
            # http://python.usyiyi.cn/documents/django_182/ref/templates/api.html
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

WSGI_APPLICATION = 'unusebamboo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django@297413',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static 文件步骤2: 引用位于STATIC_ROOT文件时的网址
# Static 文件步骤3: 开启静态文件服务
#   如果 DEBUG=True , 默认开启, 但是不使用collectstatic, 
#       而是在每一个app下面创建static目录
#   参考: http://python.usyiyi.cn/translate/django_182/howto/static-files/index.html
STATIC_URL = '/static/'
# 用于收集静态目录的绝对路径, 在执行: python manager.py collectstatic
STATIC_ROOT = 'staticfiles'
# 静态文件查找目录, 配合collectstatic一起使用, 不能和STATIC_ROOT相同
STATICFILES_DIRS = (
    'static',
)


# MEDIA
MEDIA_URL = '/media/'


# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'ilifediary2@163.com'
EMAIL_HOST_PASSWORD = 'a297413'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ilifediary2@163.com'
