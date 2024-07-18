#!/bin/bash
# Creates plugin cutter with unique labels so we can format and then reverses
# the ids to the cookiecutter identifiers and git apply the diff
set -e

# clean directory contents if exist (but don't delete .git directory)
if [ -d aiida-diff ]; then
  rm -rf cookiecutter_plugin_name
fi
cookiecutter --no-input -f . plugin_name=cookiecutter_plugin_name module_name=cookiecutter_module_name short_description=cookiecutter_short_description entry_point_prefix=cookiecutter_entry_point_prefix version=0.0.0-dev author=cookiecutter_author year=cookiecutter_year

cd cookiecutter_plugin_name
git init && git add -A && git commit -am 'init'
hatch fmt || true
# takes the diff and applies it on the cookie cutter template
git diff > patch
cp patch ..
cd ..
# git diff replacements of specified labels with cookiecutter identifiers
sed -i 's/ a\// a\/\{\{cookiecutter.plugin_name\}\}\//g' patch
sed -i 's/ b\// b\/\{\{cookiecutter.plugin_name\}\}\//g' patch
sed -i 's/cookiecutter_plugin_name/\{\{cookiecutter.plugin_name\}\}/g' patch
sed -i 's/cookiecutter_module_name/\{\{cookiecutter.module_name\}\}/g' patch
sed -i 's/cookiecutter_entry_point_prefix/\{\{cookiecutter.entry_point_prefix\}\}/g' patch
sed -i 's/cookiecutter_short_description/\{\{cookiecutter.short_description\}\}/g' patch
sed -i 's/0\.0\.0-dev/\{\{cookiecutter.version\}\}/g' patch
sed -i 's/cookiecutter_author/\{\{cookiecutter.author\}\}/g' patch
sed -i 's/cookiecutter_year/\{\{cookiecutter.year\}\}/g' patch
git apply --reject --whitespace=fix patch
