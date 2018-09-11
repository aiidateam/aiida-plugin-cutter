#!/bin/bash
if [ -x "$(command -v yapf)" ]; then
    echo "Running yapf..."
    yapf -i -r '../{{ cookiecutter.plugin_name }}/'
else
    echo "yapf not found. 'pip install yapf' to automatically \
          run formatter on generated plugin"
fi
