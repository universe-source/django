#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    os.environ.setdefault("DJANGO_COLORS", "light;error=yellow/blue,blink;notice=magenta")
    configuration = "Local"
    for arg in sys.argv:
        if arg.startswith("--configuration="):
            configuration = arg.split("--configuration=")[-1]
    os.environ.setdefault("DJANGO_CONFIGURATION", configuration)

    try:
        #  from django.core.management import execute_from_command_line
        # 进行封装了, 在导入execute_from_command_line之前调用了install函数
        from configurations.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)
