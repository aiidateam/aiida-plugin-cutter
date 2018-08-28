===============
Developer guide
===============

Running the tests
+++++++++++++++++

The following will discover and run all unit test::

    pip install -e .[testing]
    python manage.py

Continuous integration
++++++++++++++++++++++

``{{cookiecutter.plugin_name}}`` comes with a ``.travis.yml`` file for continuous integration tests on every commit using `Travis CI <http://travis-ci.org/>`_. It will:

#. run all tests for the ``django`` and ``sqlalchemy`` ORM
#. build the documentation
#. check coding style and version number (not required to pass by default)

Just enable Travis builds for the ``{{ cookiecutter.repo_name}}`` repository in your Travis account. 

Online documentation
++++++++++++++++++++

The documentation of ``{{cookiecutter.plugin_name}}``
is ready for `ReadTheDocs <https://readthedocs.org/>`_:

#. Add the ``{{ cookiecutter.repo_name}}`` repository on your RTD profile, preferably using ``{{ cookiecutter.plugin_name}}`` as the project name
#. In **Admin => Advanced settings => Requirements file** enter ``docs/requirements_for_rtd.txt``

Done.

PyPI release
++++++++++++

Your plugin is already prepared for being uploaded to the `Python Package Index <https://pypi.org/>`_.
Just register for an account and::

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*

After this, you (and everyone else) should be able to::

    pip install {{cookiecutter.plugin_name}}


