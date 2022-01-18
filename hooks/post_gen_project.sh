#!/bin/bash
if [ -x "$(command -v black)" ]; then
    echo "Running black on {{ cookiecutter.plugin_name }}"
    black '../{{ cookiecutter.plugin_name }}/'
else
    echo "black not found. 'pip install black' to automatically \
          run formatter on {{ cookiecutter.plugin_name }}"
fi

cat <<EOF

### IMPORTANT###
Register your plugin NOW by making a pull request to the AiiDA Plugin Registry
EOF
