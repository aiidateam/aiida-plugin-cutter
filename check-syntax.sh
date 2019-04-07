#!/bin/bash
set -e

cookiecutter --no-input -f . version=1.0.0a1
pip install -e aiida-diff[docs,pre-commit,testing]
cd aiida-diff
git init && git add -A
pre-commit install
pre-commit run
