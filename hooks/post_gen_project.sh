#!/bin/bash
if [ -x "$(command -v yapf)" ]; then
    echo "Running yapf on {{ cookiecutter.plugin_name }}"
    yapf -i -r '../{{ cookiecutter.plugin_name }}/'
else
    echo "yapf not found. 'pip install yapf' to automatically \
          run formatter on {{ cookiecutter.plugin_name }}"
fi

cat <<EOF

### IMPORTANT###
Register your plugin NOW by making a pull request to the AiiDA Plugin Registry
EOF
