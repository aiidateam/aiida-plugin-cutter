#!/bin/bash
if [ -x "$(command -v hatch)" ]; then
    echo "Running hatch on {{ cookiecutter.plugin_name }}"
    hatch fmt '../{{ cookiecutter.plugin_name }}/' || true
else
    echo "hatch not found. 'pip install hatch' to automatically \
          run formatter on {{ cookiecutter.plugin_name }}"
fi

cat <<EOF

### IMPORTANT###
Register your plugin NOW by making a pull request to the AiiDA Plugin Registry at

   https://aiidateam.github.io/aiida-registry/

EOF
