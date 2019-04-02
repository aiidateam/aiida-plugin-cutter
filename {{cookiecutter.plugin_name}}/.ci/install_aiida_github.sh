#!/bin/bash
cd ..
git clone https://github.com/aiidateam/aiida_core
cd aiida_core
git checkout $AIIDA_DEVELOP_GIT_HASH 
pip install -e .[docs,pre-commit,testing]
cd -
