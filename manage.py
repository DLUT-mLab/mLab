#!/usr/bin/env python
# ! coding=utf8

import os
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlab.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
