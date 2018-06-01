#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass

def hooks():
    print("""
### IMPORTANT###
Register your plugin NOW by making a pull request to the AiiDA Plugin Registry
on https://github.com/aiidateam/aiida-registry
""")
    #if read_user_yes_no(folder['question'], default_value=u'yes'):
    #else:

if __name__ == '__main__':
    hooks()
