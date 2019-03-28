[![Build Status](https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name}}) 
[![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_user}}/{{ cookiecutter.repo_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?branch=master) 
[![Docs status](https://readthedocs.org/projects/{{ cookiecutter.plugin_name }}/badge)](http://{{ cookiecutter.plugin_name }}.readthedocs.io/) 
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.plugin_name }}.svg)](https://badge.fury.io/py/{{ cookiecutter.plugin_name }})

# {{ cookiecutter.plugin_name }}

{{ cookiecutter.short_description }}

Templated using the [AiiDA plugin cutter](https://github.com/aiidateam/aiida-plugin-cutter).

## Installation

```shell
git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name}} .
cd {{ cookiecutter.repo_name }}
pip install -e .  # also installs aiida, if missing (but not postgres)
# pip install -e .[pre-commit,testing] # install extras for more features
verdi quicksetup  # better to set up a new profile
verdi plugin list aiida.calculations  # should now show your calclulation plugins
```

## Usage

Here goes a complete example of how to submit a test calculation using this plugin.

A quick demo of how to submit a calculation:
```shell
verdi daemon start         # make sure the daemon is running
cd examples
verdi run submit.py        # submit test calculation
verdi process list -a  # check status of calculation
```

The plugin also includes verdi commands to inspect its data types:
```shell
verdi data {{cookiecutter.entry_point_prefix}} list
verdi data {{cookiecutter.entry_point_prefix}} export <PK>
```

## Tests

The following will discover and run all unit tests:
```shell
pip install -e .[testing]
pytest -v
```

## License

MIT

{%if cookiecutter.contact_email!=""%}
## Contact

{{ cookiecutter.contact_email }}
{%endif%}
