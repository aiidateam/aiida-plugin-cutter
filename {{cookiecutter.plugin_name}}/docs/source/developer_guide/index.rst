===============
Developer guide
===============

Running the tests
+++++++++++++++++

The following will discover and run all unit test::

    pip install -e .[testing]
    pytest -v

Automatic coding style checks
+++++++++++++++++++++++++++++

Enable enable automatic checks of code sanity and coding style::

    pip install -e .[pre-commit]
    pre-commit install

After this, the `yapf <https://github.com/google/yapf>`_ formatter, 
the `pylint <https://www.pylint.org/>`_ linter
and the `prospector <https://pypi.org/project/prospector/>`_ code analyzer will
run at every commit.

If you ever need to skip these pre-commit hooks, just use::

    git commit -n


Continuous integration
++++++++++++++++++++++

``{{cookiecutter.plugin_name}}`` comes with a ``.github`` folder that contains continuous integration tests on every commit using `GitHub Actions <https://github.com/features/actions>`_. It will:

#. run all tests for the ``django`` ORM
#. build the documentation
#. check coding style and version number (not required to pass by default)

Online documentation
++++++++++++++++++++

The documentation of ``{{cookiecutter.plugin_name}}``
is ready for `ReadTheDocs <https://readthedocs.org/>`_:

Simply add the ``{{ cookiecutter.repo_name}}`` repository on your RTD profile, preferably using ``{{ cookiecutter.plugin_name}}`` as the project name - that's it!


PyPI release
++++++++++++

Your plugin is ready to be uploaded to the `Python Package Index <https://pypi.org/>`_.
Just register for an account and::

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*

After this, you (and everyone else) should be able to::

    pip install {{cookiecutter.plugin_name}}

You can also enable *automatic* deployment of git tags to the python package index:
simply generate a `PyPI API token <https://pypi.org/help/#apitoken>`_ for your PyPI account and add it as a secret to your GitHub repository under the name ``pypi_token`` (Go to Settings -> Secrets).
