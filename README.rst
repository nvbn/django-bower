Django-bower
============

Easy way to use `bower <http://bower.io/>`_ with your `django <https://www.djangoproject.com/>`_ project.

Installation
------------

Install django-bower package::

    pip install -e "git+https://github.com/nvbn/django-bower.git#egg=django-bower"

Add django-bower to `INSTALLED_APPS` in ypur settings::

    'djangobower',

Add staticfinder to `STATICFILES_FINDERS`::

    'djangobower.finders.BowerFinder',

Specifie path to components root (you need to use absolute path) and create it::

    BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'

You can see example settings file in `example project <https://github.com/nvbn/django-bower/blob/master/example/example/settings.py>`_.

Usage
-----

Specifie `BOWER_INSTALLED_APPS` in settings, like::

    BOWER_INSTALLED_APPS = (
        'jquery',
        'underscore',
    )

Download bower packages with management command::

    ./manage.py bower_install

Add scripts in template, like::

    {% load static %}
    <script type="text/javascript" src='{% static 'jquery/jquery.js' %}'></script>

In production you need to call `bower_install` before `collectstatic`::

    ./manage.py bower_install
    ./manage.py collectstatic

Running tests
-------------

For running tests you need to install `django-bower` in development mode with::

    python setup.py develop

Now you can run tests with::

    django-admin.py test --settings=djangobower.test_settings djangobower

Example project
---------------

For running example project you need to change dir to `example`.
Prepare project with::

    ./manage.py syncdb
    ./manage.py bower_install

And run project with::

    ./manage.py runserver
