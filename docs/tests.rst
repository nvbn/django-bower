*************
Running tests
*************

For running tests you need to install `django-bower` in development mode with:

.. code-block:: bash

    python setup.py develop

Install dev requirements:

.. code-block:: bash

    pip install -r requirements_dev.txt

Now you can run tests with:

.. code-block:: bash

    django-admin.py test --settings=djangobower.test_settings djangobower

You can change test project root with `TEST_PROJECT_ROOT` environment variable. By default it is `/tmp`.

You can show current tests status in `travis ci <https://travis-ci.org/nvbn/django-bower/>`_.
