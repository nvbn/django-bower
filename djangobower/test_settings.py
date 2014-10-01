import os



TEST_PROJECT_ROOT = os.path.abspath(
    os.environ.get('TEST_PROJECT_ROOT', '/tmp/'),
)

BASE_DIR = TEST_PROJECT_ROOT

BOWER_COMPONENTS_ROOT = os.path.join(TEST_PROJECT_ROOT, 'bower_components')

STATIC_ROOT = os.path.join(TEST_PROJECT_ROOT, 'bower_static')

STATIC_URL = '/static/'

BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'underscore',
)

SECRET_KEY = 'iamdjangobower'

INSTALLED_APPS = (
    'djangobower',
)

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
