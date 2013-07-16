*****
Usage
*****

Specifie `BOWER_INSTALLED_APPS` in settings, like::
    .. code-block:: python

        BOWER_INSTALLED_APPS = (
            'jquery#1.9',
            'underscore',
        )

Download bower packages with management command::
    .. code-block:: bash

        ./manage.py bower_install

Add scripts in template, like::
    .. code-block:: html+django

        {% load static %}
        <script type="text/javascript" src='{% static 'jquery/jquery.js' %}'></script>

In production you need to call `bower_install` before `collectstatic`::
    .. code-block:: bash

        ./manage.py bower_install
        ./manage.py collectstatic

You can use `bower_freeze` to receive `BOWER_INSTALLED_APPS` with fixed current versions::
    .. code-block:: bash

        ./manage.py bower_freeze
