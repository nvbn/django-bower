*************
Running tests
*************

For running tests you need to install `django-bower` in development mode with::
    .. code-block:: bash

        python setup.py develop

Now you can run tests with::
    .. code-block:: bash

        django-admin.py test --settings=djangobower.test_settings djangobower
