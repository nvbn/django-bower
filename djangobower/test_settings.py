import os
import django

TEST_PROJECT_ROOT = os.path.abspath(
    os.environ.get('TEST_PROJECT_ROOT', '/tmp/'),
)

BOWER_COMPONENTS_ROOT = os.path.join(TEST_PROJECT_ROOT, 'bower_components')

STATIC_ROOT = os.path.join(TEST_PROJECT_ROOT, 'bower_static')

STATIC_URL = '/static/'

BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
)

SECRET_KEY = 'iamdjangobower'

INSTALLED_APPS = [
    'djangobower',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if django.VERSION[0] == 1 and django.VERSION[1] < 6:
    INSTALLED_APPS.append('discover_runner')
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
