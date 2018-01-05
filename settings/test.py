# -*- coding: utf-8 -*-
'''
Test Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
from .common import Common


class Test(Common):

    SECRET_KEY = 'w*0cz+h$%@l841$x(wfkcd0dm2f!4$dwb+v2rn!hk+uvjtestt'

    DEBUG = True
    LOCAL = True
    SETTING = 'Test'

    INSTALLED_APPS = ['test_without_migrations'] + list(Common.INSTALLED_APPS)
    TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'

    # DATABASE CONFIGURATION
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test',
        }
    }
    CACHE_QUERY = False
    # END DATABASE CONFIGURATION
