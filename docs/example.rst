***************
Example project
***************

For running example project you need to change dir to `example`.

Prepare project with:

.. code-block:: bash

    ./manage.py syncdb
    ./manage.py bower_install
    ./manage.py collectstatic

And run project with:

.. code-block:: bash

    ./manage.py runserver
