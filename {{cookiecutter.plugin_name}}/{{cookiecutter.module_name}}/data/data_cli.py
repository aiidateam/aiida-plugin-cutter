import sys
import click
from aiida.cmdline.commands import data_cmd
from aiida.cmdline.dbenv_lazyloading import load_dbenv_if_not_loaded


# See aiida.cmdline.data entry point in setup.json
@data_cmd.group('{{cookiecutter.entry_point_prefix}}.factors')
def cli():
    """Command line interface for {{cookiecutter.plugin_name}}"""
    pass


@cli.command('list')
def list_():  # pylint: disable=redefined-builtin
    """
    Display all MultiplyParameters nodes
    """
    load_dbenv_if_not_loaded(
    )  # Important to load the dbenv in the last moment

    from aiida.orm.querybuilder import QueryBuilder
    from aiida.orm import DataFactory
    MultiplyParameters = DataFactory('{{cookiecutter.entry_point_prefix}}.factors')

    qb = QueryBuilder()
    qb.append(MultiplyParameters)
    results = qb.all()

    s = ""
    for result in results:
        obj = result[0]
        s += "{}, pk: {}\n".format(str(obj), obj.pk)
    sys.stdout.write(s)


@cli.command('export')
@click.option(
    '--outfile',
    '-o',
    type=click.Path(dir_okay=False),
    help='Write output to file (default: print to stdout).')
@click.argument('pk', type=int)
def export(outfile, pk):
    """Export a MultiplyParameters node, identified by PK, to plain text"""
    load_dbenv_if_not_loaded(
    )  # Important to load the dbenv in the last moment

    from aiida.orm import load_node
    node = load_node(pk)
    string = str(node)

    if outfile:
        with open(outfile, 'w') as f:
            f.write(string)
    else:
        click.echo(string)
