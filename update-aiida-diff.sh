#!/bin/bash
# Creates default aiida-diff output of plugin cutter
# Helps with updating aiida-diff git repository by adding only changed files to git
set -e

# clean directory contents if exist (but don't delete .git directory)
if [ -d aiida-diff ]; then
  rm -rf aiida-diff/*
else
  git clone https://github.com/aiidateam/aiida-diff
fi

cookiecutter --no-input -f . version=1.2.0
cd aiida-diff
git init && git add -A
hatch fmt
