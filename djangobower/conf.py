import os, sys

from django.conf import settings

COMPONENTS_ROOT = getattr(settings, 'BOWER_COMPONENTS_ROOT', os.path.join(settings.BASE_DIR, 'bower_components'))

BOWER_PATH_DEFAULT = 'bower'
if sys.platform == 'win32':
	BOWER_PATH_DEFAULT = os.path.join(os.getenv("APPDATA"), 'npm', 'bower.cmd')

BOWER_PATH = getattr(settings, 'BOWER_PATH', BOWER_PATH_DEFAULT)
