"""
Utility functions for aiida plugins.

Useful for:
 * compatibility with different aiida versions

"""
from __future__ import absolute_import

import aiida
from distutils.version import StrictVersion # pylint: disable=no-name-in-module,import-error

AIIDA_VERSION = StrictVersion(aiida.get_version())

def load_verdi_data():
    """Load the verdi data click command group for any version since 0.11."""
    verdi_data = None
    import_errors = []

    try:
        from aiida.cmdline.commands import data_cmd as verdi_data
    except ImportError as err:
        import_errors.append(err)

    if not verdi_data:
        try:
            from aiida.cmdline.commands import verdi_data
        except ImportError as err:
            import_errors.append(err)

    if not verdi_data:
        try:
            from aiida.cmdline.commands.cmd_data import verdi_data
        except ImportError as err:
            import_errors.append(err)

    if not verdi_data:
        err_messages = '\n'.join(
            [' * {}'.format(_err) for _err in import_errors])
        raise ImportError(
            'The verdi data base command group could not be found:\n' +
            err_messages)

    return verdi_data

def load_dbenv_if_not_loaded():
    # pylint: disable=import-error
    if AIIDA_VERSION < StrictVersion('1.0a0'):
        from aiida.cmdline.dbenv_lazyloading import load_dbenv_if_not_loaded as fn
        return fn()

    from aiida.cmdline.utils.decorators import load_dbenv_if_not_loaded as fn
    return fn()
