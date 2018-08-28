#!/bin/bash
set -ex

if [ "$TEST_TYPE" == "docs" ] ; then 
    cd docs
    make
elif [ "$TEST_TYPE" == "pre-commit" ] ; then 
    git init
    git add -A
    pre-commit install
    pre-commit run --all-files || ( git status --short ; git diff ; exit 1 )
else
    pytest -v
fi
