Django-bower
============

.. image:: https://travis-ci.org/nvbn/django-bower.png
   :alt: Build Status
   :target: https://travis-ci.org/nvbn/django-bower
.. image:: https://coveralls.io/repos/nvbn/django-bower/badge.png?branch=develop
   :alt: Coverage Status
   :target: https://coveralls.io/repos/nvbn/django-bower
.. image:: https://pypip.in/v/django-bower/badge.png
   :target: https://crate.io/packages/django-bower/
.. image:: https://pypip.in/d/django-bower/badge.png
   :target: https://crate.io/packages/django-bower/

Easy way to use `bower <http://bower.io/>`_ with your `django <https://www.djangoproject.com/>`_ project.

Bower is a package manager for the web. It offers a generic, unopinionated solution to the problem of front-end package management, while exposing the package dependency model via an API that can be consumed by a more opinionated build stack. There are no system wide dependencies, no dependencies are shared between different apps, and the dependency tree is flat.

Read full documentation on `read-the-docs <https://django-bower.readthedocs.org/en/latest/>`_.

Installation
------------

Install django-bower package:

.. code-block:: bash

    pip install django-bower

Add django-bower to `INSTALLED_APPS` in your settings:

.. code-block:: python

    'djangobower',

Add staticfinder to `STATICFILES_FINDERS`:

.. code-block:: python

    'djangobower.finders.BowerFinder',

Specifie path to components root (you need to use absolute path):

.. code-block:: python

    BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'


If you need, you can manually set path to bower

.. code-block:: python

    BOWER_PATH = '/usr/bin/bower'

You can see example settings file in `example project <https://github.com/nvbn/django-bower/blob/master/example/example/settings.py>`_.

Usage
-----

Specifie `BOWER_INSTALLED_APPS` in settings, like:

.. code-block:: python

    BOWER_INSTALLED_APPS = (
        'jquery#1.9',
        'underscore',
    )

Download bower packages with management command:

.. code-block:: bash

    ./manage.py bower_install

Add scripts in template, like:

.. code-block:: html+django

    {% load static %}
    <script type="text/javascript" src='{% static 'jquery/jquery.js' %}'></script>

In production you need to call `bower_install` before `collectstatic`:

.. code-block:: bash

    ./manage.py bower_install
    ./manage.py collectstatic

You can use `bower_freeze` to receive `BOWER_INSTALLED_APPS` with fixed current versions:

.. code-block:: bash

    ./manage.py bower_freeze

Python 3 support
----------------
django-bower support python 3.3+
