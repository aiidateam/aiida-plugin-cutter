#!/bin/bash
if [ -x "$(command -v yapf)" ]; then
    echo "Running yapf formatter..."
    yapf -i -r '../{{ cookiecutter.plugin_name }}/'
fi
