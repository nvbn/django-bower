*****
Usage
*****

Specifie `BOWER_INSTALLED_APPS` in settings, like:

.. code-block:: python

    BOWER_INSTALLED_APPS = (
        'jquery#1.9',
        'underscore',
    )

Download bower packages with management command:

.. code-block:: bash

    ./manage.py bower install

Add scripts in template, like:

.. code-block:: html+django

    {% load static %}
    <script type="text/javascript" src='{% static 'jquery/jquery.js' %}'></script>

In production you need to call `bower install` before `collectstatic`:

.. code-block:: bash

    ./manage.py bower install
    ./manage.py collectstatic

If you need to pass arguments to bower, like `--allow-root`, use:

.. code-block:: bash

    ./manage.py bower install -- --allow-root

You can use `bower freeze` to receive `BOWER_INSTALLED_APPS` with fixed current versions:

.. code-block:: bash

    ./manage.py bower freeze

You can call bower commands like `info` and `update` with:

.. code-block:: bash

    ./manage.py bower info backbone
    ./manage.py bower update
