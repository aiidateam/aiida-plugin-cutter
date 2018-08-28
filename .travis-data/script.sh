#!/bin/bash
set -ex

if [ "$TEST_TYPE" == "docs" ] ; then 
    cd $PLUGIN_DIR/docs
    make
elif [ "$TEST_TYPE" == "pre-commit" ] ; then 
    cd $PLUGIN_DIR
    git init
    git add -A
    pre-commit install
    pre-commit run --all-files || ( git status --short ; git diff ; exit 1 )
else
    cd $PLUGIN_DIR
    pytest -v
fi
