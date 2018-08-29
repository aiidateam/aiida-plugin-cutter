#!/bin/bash
if hash yapf 2>/dev/null; then
    echo "Running yapf formatter..."
    yapf -i -r '../{{ cookiecutter.plugin_name }}/'
fi
