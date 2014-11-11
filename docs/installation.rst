************
Installation
************

Install `bower <http://bower.io/>`_ from npm:

.. code-block:: bash

    npm install -g bower

And django-bower package:

.. code-block:: bash

    pip install django-bower

Add django-bower to `INSTALLED_APPS` in your settings:

.. code-block:: python

    'djangobower',

Add staticfinder to `STATICFILES_FINDERS`:

.. code-block:: python

    'djangobower.finders.BowerFinder',

Specify path to components root (you need to use absolute path):

.. code-block:: python

    BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'

If you need, you can manually set path to bower

.. code-block:: python

    BOWER_PATH = '/usr/bin/bower'

Example settings file with django-bower:

.. code-block:: python
    :linenos:

    import os


    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), ".."),
    )

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    STATIC_URL = '/static/'

    BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'djangobower.finders.BowerFinder',
    )

    SECRET_KEY = 'g^i##va1ewa5d-rw-mevzvx2^udt63@!xu$-&di^19t)5rbm!5'

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    ROOT_URLCONF = 'example.urls'

    WSGI_APPLICATION = 'example.wsgi.application'

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'templates'),
    )

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'djangobower',
    )

    BOWER_INSTALLED_APPS = (
        'jquery',
        'underscore',
    )
