[![Build Status](https://github.com/aiidateam/aiida-plugin-cutter/workflows/aiida-plugin-cutter/badge.svg?branch=master)](https://github.com/aiidateam/aiida-plugin-cutter/actions)

# AiiDA plugin cutter

Cookie cutter recipe for [AiiDA](http://www.aiida.net) plugins.

The fastest most convenient way for getting started with developing AiiDA plugins.

For the default output of the plugin cutter, see the [aiida-diff](https://github.com/aiidateam/aiida-diff) demo plugin.

Note: This cuts plugins for `aiida-core>=1.0.0`. 
See the `support/aiida-0.x` branch for cutting plugins for older versions of `aiida-core`.

## Usage

    pip install cookiecutter yapf
    cookiecutter https://github.com/aiidateam/aiida-plugin-cutter.git

![Demo](https://image.ibb.co/ct6rL8/aiida_plugin_cutter.gif "The fastest way to kickstart an AiiDA plugin.")

This will produce the files and folder structure for your plugin,
already adjusted for the name of your plugin.

## Features

Plugins templated using the plugin cutter

* include a calculation, parser and data type as well as an example of
  how to submit a calculation
* include basic regression tests using the [pytest](https://docs.pytest.org/en/latest/) framework ( (submitting a calculation, ...)
* can be directly pip-installed (and are prepared for submisson to [PyPI](https://pypi.org/)
* include a documentation template ready for [Read the Docs](http://aiida-plugin-template.readthedocs.io/en/latest/)
* come with [Github Actions](https://github.com/features/actions) configuration - enable it to run tests and check test coverage at every commit
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

## Acknowledgements

This work is supported by the [MARVEL National Centre for Competency in
Research](<http://nccr-marvel.ch>) funded by the [Swiss National
Science Foundation](<http://www.snf.ch/en>), as well as by the [MaX
European Centre of Excellence](<http://www.max-centre.eu/>) funded by
the Horizon 2020 EINFRA-5 program, Grant No. 676598.

![MARVEL](miscellaneous/logos/MARVEL.png)
![MaX](miscellaneous/logos/MaX.png)
