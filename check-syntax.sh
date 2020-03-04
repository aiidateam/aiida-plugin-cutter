#!/bin/bash
set -e

# clean directory contents if exist (but don't delete .git directory)
if [ -d aiida-diff ]; then
  rm -rf aiida-diff/*
fi

cookiecutter --no-input -f . version=1.1.1
pip install -e aiida-diff[docs,pre-commit,testing]
cd aiida-diff
git init && git add -A
pre-commit install
pre-commit run
