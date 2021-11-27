"""Defines Two Point Science MissingData class.

Used to indicate data points are missing from Two Point Hospital research.

    Typical usage example:
    MISSING_DATA = MissingData("TO DO: DON'T DO NOW... Get this data")
    # See: help(tps.tph_constants) for the rest...
"""

# Standard Imports

# Third Party Imports
from typing import Any

# Local Imports


class MissingData(object):
    """Intended for use as an UNDEFINED macro.

    Typical usage example:
    MISSING_DATA = MissingData()

    if some_data and some_data == MissingData():
        print('Data point should be researched and then defined')
    else:
        print(f'Data point is {some_data}')
    """

    def __init__(self, data: Any = None) -> None:
        """MissingData class ctor."""
        self._data = data  # Internal data

    def __eq__(self, other) -> bool:
        """Override the == operator."""
        # LOCAL VARIABLES
        the_same = False

        # COMPARE
        if isinstance(other, MissingData):
            if self._data == other._data:
                the_same = True

        # DONE
        return the_same
