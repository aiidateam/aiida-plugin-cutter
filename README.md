# AiiDA plugin cutter

Cookie cutter recipe for [AiiDA](http://www.aiida.net) plugins.

The fastest most convenient way for getting started with developing AiiDA plugins.

For the default output of the plugin cutter, see the [aiida-diff](https://github.com/aiidateam/aiida-diff) demo plugin.

## Usage

    pip install cookiecutter yapf
    cookiecutter https://github.com/aiidateam/aiida-plugin-cutter.git

![Demo](https://image.ibb.co/ct6rL8/aiida_plugin_cutter.gif "The fastest way to kickstart an AiiDA plugin.")

This will produce the files and folder structure for your plugin,
already adjusted for the name of your plugin.

## Features

Plugins templated using the plugin cutter

* can be directly pip-installed (and are prepared for submisson to [PyPI](https://pypi.org/)
* include basic regression tests (submitting a calculation)
* include a documentation template ready for [Read the Docs](http://aiida-plugin-template.readthedocs.io/en/latest/)
* come with [Travis CI](https://travis-ci.org) configuration - enable it to run tests and check test coverage at every commit
* come with pre-commit hooks that sanitize coding style and check for syntax errors - enable via `pre-commit install`

For more information on how to take advantage of these features, 
see the [developer guide](https://aiida-diff.readthedocs.io/en/latest/developer_guide) of your plugin.

## Developing the plugin cutter

The plugin cutter comes with rather strict continuous integration tests which

 * test that the cookiecutter recipe works
 * test that the plugin can be pip-installed
 * test that the unit tests of the plugin pass
 * test that the documentation of the plugin builds
 * test that the code of the plugin confirms to coding standards

Particularly the last test is easy to break. In order to check your syntax run
```
cookiecutter --no-input -f .
pip install -e aiida-diff[docs,pre-commit,testing]
cd aiida-diff
git init && git add -A
pre-commit install
pre-commit run
```
or simply: `./check-syntax.sh`


## License

MIT

## Contact

Please report issues to the GitHub issue tracker. Other inquiries may be
directed to the [AiiDA mailinglist](http://www.aiida.net/mailing-list/).
