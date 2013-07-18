from django.conf import settings


COMPONENTS_ROOT = getattr(settings, 'BOWER_COMPONENTS_ROOT')
BOWER_PATH = getattr(settings, 'BOWER_PATH', 'bower')
