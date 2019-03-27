"""
{{cookiecutter.module_name}}

{{cookiecutter.short_description}}
"""

from __future__ import absolute_import

__version__ = "{{cookiecutter.version}}"

# disable psycopg2 warning
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='psycopg2')
