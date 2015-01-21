# -*- coding: utf-8 -*-
import os
import sys
from django.conf import settings

__all__ = ['COMPONENTS_ROOT', 'BOWER_PATH']

COMPONENTS_ROOT = getattr(settings, 'BOWER_COMPONENTS_ROOT', os.path.abspath(os.path.dirname(__name__)))

if sys.platform == 'win32':
    default_bower_path = os.path.join(os.getenv("APPDATA"), 'npm', 'bower.cmd')
else:
    default_bower_path = 'bower'

BOWER_PATH = getattr(settings, 'BOWER_PATH', default_bower_path)
