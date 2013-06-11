BOWER_COMPONENTS_ROOT = '/tmp/bower_components/'

STATIC_ROOT = '/tmp/bower_static/'

STATIC_URL = '/static/'

BOWER_INSTALLED_APPS = (
    'jquery',
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
