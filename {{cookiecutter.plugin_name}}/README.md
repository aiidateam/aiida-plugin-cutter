# {{ cookiecutter.plugin_name }}

{{ cookiecutter.short_description }}

Templated using the [AiiDA plugin cutter](https://github.com/aiidateam/aiida-plugin-cutter).

## Installation

```shell
git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name}} .
cd {{ cookiecutter.repo_name }}
pip install -e .  # also installs aiida, if missing (but not postgres)
#pip install -e .[precommit,testing] # install extras for more features
verdi quicksetup  # better to set up a new profile
verdi calculation plugins  # should now show your calclulation plugins
```

## Usage

Here goes a complete example of how to submit a test calculation using this plugin.

A quick demo of how to submit a calculation:
```shell
verdi daemon start         # make sure the daemon is running
cd examples
verdi run submit.py        # submit test calculation
verdi calculation list -a  # check status of calculation
```

If you have already set up your own {{cookiecutter.module_name}} code using `verdi code setup`, you may want to try the following command:
```
{{cookiecutter.entry_point_prefix}}-submit  # uses {{cookiecutter.module_name}}.cli
```

## Tests

The following will discover and run all unit test:
```shell
pip install -e .[testing]
python manage.py
```

## License

MIT

## Contact

{{ cookiecutter.contact_email }}
