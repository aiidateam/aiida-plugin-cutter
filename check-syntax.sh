#!/bin/bash
set -e

cookiecutter --no-input -f .
pip install -e aiida-diff[docs,pre-commit,testing]
cd aiida-diff
git init && git add -A
pre-commit install
pre-commit run
