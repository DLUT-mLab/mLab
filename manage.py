#!/usr/bin/env python
# ! coding=utf8

import os
import sys

#  default_encoding = 'utf-8'
#  if sys.getdefaultencoding() != default_encoding:
    #  reload(sys)
    #  sys.setdefaultencoding(default_encoding)
from mlab.settings import BASE_DIR, INSTALLED_APPS

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlab.settings")

    from django.core.management import execute_from_command_line

    if sys.argv[1] == 'clearmigrations':
        for app in INSTALLED_APPS:
            app_path = os.path.join(BASE_DIR, *app.split('.'))
            migrations = os.path.join(app_path, 'migrations')
            if os.path.exists(migrations):
                for mg in os.listdir(migrations):
                    os.remove(os.path.join(migrations, mg))
                open(os.path.join(migrations, '__init__.py'), 'w+').close()
    elif sys.argv[1] == 'initmigrations':
        # some hack by liangzi
        argv = sys.argv[:1]
        argv.append('makemigrations')
        for app in INSTALLED_APPS:
            argv.append(app.split('.')[-1])
        execute_from_command_line(argv)
    else:
        execute_from_command_line(sys.argv)

