# -*- coding: utf-8 -*-

# you can directly subclass aiida.orm.data.Data
# or any other data type listed under 'verdi data'
from aiida.orm.data.parameter import ParameterData


class MultiplyParameters(ParameterData):
    """
    Input parameters for multiply calculation.
    """

    def __init__(self, x1=1, x2=1, **kwargs):
        """
        Constructor for the data class

        Usage: ``MultiplyParameters(x1=3, x2=4)``

        .. note:: As of 2017-09, the constructor must also support a single dbnode
          argument (to reconstruct the object from a database node).
          For this reason, positional arguments are not allowed.
        """
        if 'dbnode' in kwargs:
            super(MultiplyParameters, self).__init__(**kwargs)
        else:
            # set dictionary of ParameterData
            input_dict = {'x1': x1, 'x2': x2}
            super(MultiplyParameters, self).__init__(dict=input_dict, **kwargs)

    @property
    def x1(self):
        """
        The value for ``x1`` (the first number to multiply)
        """
        return self.get_attr('x1', None)

    @property
    def x2(self):
        """
        The value for ``x2`` (the second number to multiply)
        """
        return self.get_attr('x2', None)

    def __str__(self):
        """
        Return the two values ``x1`` and ``x2`` as a string
        """
        s = "x1: {}, x2: {}".format(self.x1, self.x2)
        return s
