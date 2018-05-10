#!/usr/bin/env python


def multiply():
    """
    Example code, multiplying two numbers.

    This is expected to be run from the command line, as it reads
    ``sys.argv``.

    Usage::

      ./code.py in_file out_file

    Reads input from ``in_file`` (``sys.argv[1]``) (e.g.: {"x1": 2, "x2": 4})
    Writes product to ``out_file`` (``sys.argv[2]``) (e.g.: {"product": 8})
    
    Note for developers:

    * This would be replaced by a python wrapper around your code.
    * This code will be executed on the computer you specify.
    """
    import json
    import sys

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file) as f:
        in_dict = json.load(f)

    out_dict = {'product': in_dict['x1'] * in_dict['x2']}

    with open(out_file, 'w') as f:
        json.dump(out_dict, f)

    print("Exiting multiply code.")


if __name__ == '__main__':
    multiply()
