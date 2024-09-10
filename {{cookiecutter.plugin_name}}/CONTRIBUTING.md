### Tests

Tests can be run in different ways
```
hatch test # Run tests whith your current python version 
hatch test --python 3.9 # Run tests for python version 3.9
hatch test --show # See all defined test environment
hatch test --all # Run tests for all test environments 
hatch test --coverage # Run tests with coverage
```
You can add arbitrary flags to pytest at the end of the command. For example to run the tests in debug mode use
```
hatch test --pdb 
```
We use ipdb as debugger backend for autocompletion.

### Static code analysis

To check the formatting and linting run
```
hatch fmt --check
```
If you want to automatically fix errors that are fixable run
```
hatch fmt
```
If you want to run this command before each commit, please install the pre-commit hook
```
pip install .[pre-commit]
pre-commit install
```
You can also run the linter and formatter separately
```
hatch fmt --formatter
hatch fmt --linter
```

### Building the docs

Please run
```
hatch run docs:build
```

### Build and publishing package

To build and publish a package please use
```
hatch build
hatch publish -r test # test pypi
hatch publish # pypi
```
