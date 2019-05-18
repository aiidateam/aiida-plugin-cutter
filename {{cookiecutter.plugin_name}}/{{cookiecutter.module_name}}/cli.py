"""
Command line interface (cli) for {{cookiecutter.module_name}}.

Register new commands either via the "console_scripts" entry point or plug them
directly into the 'verdi' command by using AiiDA-specific entry points like
"aiida.cmdline.data" (both in the setup.json file).
"""

from __future__ import absolute_import
import sys
import click
from aiida.cmdline.utils import decorators
from aiida.cmdline.commands.cmd_data import verdi_data
from aiida.cmdline.params.types import DataParamType


# See aiida.cmdline.data entry point in setup.json
@verdi_data.group('{{cookiecutter.entry_point_prefix}}')
def data_cli():
    """Command line interface for {{cookiecutter.plugin_name}}"""
    pass


@data_cli.command('list')
@decorators.with_dbenv()
def list_():  # pylint: disable=redefined-builtin
    """
    Display all DiffParameters nodes
    """
    from aiida.orm import QueryBuilder
    from aiida.plugins import DataFactory
    DiffParameters = DataFactory('{{cookiecutter.entry_point_prefix}}')

    qb = QueryBuilder()
    qb.append(DiffParameters)
    results = qb.all()

    s = ""
    for result in results:
        obj = result[0]
        s += "{}, pk: {}\n".format(str(obj), obj.pk)
    sys.stdout.write(s)


@data_cli.command('export')
@click.argument('node', metavar='IDENTIFIER', type=DataParamType())
@click.option('--outfile',
              '-o',
              type=click.Path(dir_okay=False),
              help='Write output to file (default: print to stdout).')
@decorators.with_dbenv()
def export(node, outfile):
    """Export a DiffParameters node (identified by PK, UUID or label) to plain text."""
    string = str(node)

    if outfile:
        with open(outfile, 'w') as f:
            f.write(string)
    else:
        click.echo(string)
