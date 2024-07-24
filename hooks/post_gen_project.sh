#!/bin/bash
if [ -x "$(command -v hatch)" ]; then
    echo "Running hatch on {{ cookiecutter.plugin_name }}"
    # For some reason we need to invoke the formatting twice to be effective
    hatch fmt || true
    hatch fmt || true
else
    echo "hatch not found. 'pip install hatch' to automatically \
          run formatter on {{ cookiecutter.plugin_name }}"
fi

cat <<EOF

### IMPORTANT###
Register your plugin NOW by making a pull request to the AiiDA Plugin Registry at

   https://aiidateam.github.io/aiida-registry/

EOF
