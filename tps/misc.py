"""Defines miscellaneous Two Point Science functionality.

Defines some general use functionality used in the package.

    Typical usage example:

    from tps.tph_misc import clear_screen, print_exception
    try:
        clear_screen()
    except Exception as err:
        print_exception(err)
"""

# Standard Imports
from collections import OrderedDict
import subprocess
import sys

# Third Party Imports
from typing import Any
import platform

# Local Imports
# from tps.tph_constants import TPH_ROOM_DICT


def clear_screen() -> None:
    """OS-agnostic screen clear.

    Determines the operating system and clears the screen using an OS-appropriate command through
    subprocess.  Defaults to 60 blank lines if it can't determine the operating system.
    """
    # LOCAL VARIABLES
    os_name = platform.system()  # Operating system name

    # CLEAR IT
    if os_name in ('Linux', 'Darwin'):
        command = 'clear'
    elif os_name == 'Windows':
        command = 'cls'
    else:
        for _ in range(0, 60):
            print('\n')
        return

    subprocess.call([command], shell=True)


def print_exception(error: Exception) -> str:
    """Standardizes exception messages and prints to stderr.

    Determines error exception type and formats the message with message_template.

    Args:
        error: Exception (or a class inherited from it) object.

    Returns:
        A string containing the formatted exception message.

    Raises:
        TypeError: error is not an Exception (or inherited from) type.
    """
    # LOCAL VARIABLES
    exception_type = ''                # Human-readable Exception type (e.g., Value)
    message_template = '{} ERROR: {}'  # Template message format
    exception_str = ''                 # Human-readable exception message
    formatted_msg = ''                 # End result message to return

    # INPUT VALIDATION
    if not isinstance(error, Exception):
        raise ValueError(f'Argument error was not an Exception but contained {repr(error)}')

    # FORMAT
    if isinstance(error, FileNotFoundError):
        exception_type = 'FILE'
    elif isinstance(error, OSError):
        exception_type = 'OS'
    elif isinstance(error, RuntimeError):
        exception_type = 'RUNTIME'
    elif isinstance(error, TypeError):
        exception_type = 'TYPE'
    elif isinstance(error, ValueError):
        exception_type = 'VALUE'
    else:
        exception_type = 'GENERAL'

    # PRINT
    # Str wrapper is important in case error.args[0] contains an errno value
    if isinstance(error, FileNotFoundError):
        exception_str = str(error)
    else:
        exception_str = str(error.args[0])
    formatted_msg = message_template.format(exception_type, exception_str)
    print(formatted_msg, file=sys.stderr)

    # DONE
    return formatted_msg


def print_edge_table(edge_dict: dict, room_lookup: dict, sort_by_count: bool = True,
                     sort_desc: bool = True) -> None:
    """Prints the room connection (edge) table.

    For normal use cases, use enumerate_edges() from tps.dgraph to construct the edge_dict and
    use TPH_ROOM_DICT from tps.tph_constants as the room_lookup.

    Args:
        edge_dict: Dictionary containing room names as keys and room counts as values.
        room_lookup: Dictionary containing room names as keys and RoomDetails as values.
        sort_by_count: Optional; If True, sort the table by room count.  Otherwise, sorts by name.
        sort_desc: Optional; If True, sort the table in descending order.  Otherwise, table is
            sorted in ascending order.

    Raises:
        TypeError: Bad data type passed in.
        ValueError: Invalid value found in the arguments.
    """
    # LOCAL VARIABLES
    local_dict = OrderedDict()  # List of sorted keys from edge_dict
    # temp_list = []            # List of sorted tuples formed from just the dictionary
    tuple_list = []             # List of sorted tuples formed from dictionary entries and lookups
    temp_room_details = None    # Temporary RoomDetails namedtuple
    temp_room_purpose = ''      # Temporary RoomDetails.purpose

    # INPUT VALIDATION
    # print(f'EDGE DICT: {edge_dict}')  # DEBUGGING
    # print(f'ROOM LOOKUP: {room_lookup}')  # DEBUGGING
    # edge_dict
    if not isinstance(edge_dict, dict):
        raise TypeError(f'The edge_dict argument must of type dict instead of {type(edge_dict)}')
    # room_lookup
    if not isinstance(room_lookup, dict):
        raise TypeError('The room_lookup argument must of type dict instead of '
                        f'{type(room_lookup)}')
    # sort_by_count
    if not isinstance(sort_by_count, int):
        raise TypeError(f'The sort_by_count argument can not be of type {type(sort_by_count)}')
    # sort_desc
    if not isinstance(sort_desc, bool):
        raise TypeError(f'The sort_desc argument must of type bool instead of {type(sort_desc)}')

    # DO IT
    # 1. Form Table Entries
    # Sort dictionary
    if sort_by_count:
        if sort_desc:
            local_dict = OrderedDict(sorted(edge_dict.items(), reverse=False))
        else:
            local_dict = OrderedDict(sorted(edge_dict.items(), reverse=True))
        local_dict = OrderedDict(sorted(local_dict.items(), reverse=sort_desc,
                                        key=lambda item: item[1]))
    else:
        local_dict = OrderedDict(sorted(edge_dict.items(), reverse=sort_desc))
    # Form the list of tuples
    for key, value in local_dict.items():
        # Find the room purpose
        temp_room_details = _loose_lookup(room_lookup, key)
        if temp_room_details:
            try:
                temp_room_purpose = temp_room_details.purpose
            except AttributeError:
                temp_room_purpose = 'Unspecified'
        else:
            temp_room_purpose = 'Not Found'
        tuple_list.append(tuple((key, temp_room_purpose, value)))
    # 2. Print Table
    # print(f'TUPLE LIST: {tuple_list}')  # DEBUGGING
    _print_table(tuple_list, tuple(('ROOM', 'PURPOSE', 'COUNT')))


def _loose_lookup(haystack: dict, needle: str) -> Any:
    # LOCAL VARIABLES
    found_it = None  # Return value

    # INPUT VALIDATION
    # haystack
    if not isinstance(haystack, dict):
        raise TypeError(f'The haystack argument must of type dict instead of {type(haystack)}')
    # needle
    if not isinstance(needle, str):
        raise TypeError(f'The needle argument must be of type str instead of {type(needle)}')

    # FIND IT
    for key, value in haystack.items():
        if needle.lower().startswith(key.lower()):
            found_it = value
            break

    # DONE
    return found_it


def _print_table(tuple_list: list, col_headers: tuple) -> None:
    # LOCAL VARIABLES
    longest_line = 0  # Longest line to print
    col_widths = []   # A list of maximum column widths
    num_columns = 0   # Number of columns to print
    temp_line = ''    # Dynamically built string to print one line

    # INPUT VALIDATION
    num_columns = _validate_print_table(tuple_list=tuple_list, col_headers=col_headers)

    # SIZE IT
    # Column Widths
    for width in range(0, num_columns):
        col_widths.append(0)
    # Tuple List Indices
    for entry in tuple_list:
        for index in range(0, num_columns):
            if len(str(entry[index])) + 1 > col_widths[index]:
                col_widths[index] = len(str(entry[index])) + 1
    # Column Header Indices
    for index in range(0, num_columns):
        if len(col_headers[index]) + 1 > col_widths[index]:
            col_widths[index] = len(col_headers[index]) + 1

    # Longest Line
    for width in col_widths:
        longest_line = longest_line + width

    # PRINT IT
    # 1. Header
    temp_line = '\n'  # Reset temp variable
    for index in range(0, num_columns):
        temp_line = temp_line + '{0: <{width}}'.format(col_headers[index], width=col_widths[index])
    print(temp_line)
    # 2. Separator
    print('-' * longest_line)
    # 3. Table Entries
    for entry in tuple_list:
        temp_line = ''  # Reset temp variable
        for index in range(0, num_columns):
            temp_line = temp_line + '{0: <{width}}'.format(entry[index], width=col_widths[index])
        print(temp_line)


def _validate_print_table(tuple_list: list, col_headers: tuple) -> int:
    """Validate arguments on behalf of _print_table() and returns number of columns."""
    # LOCAL VARIABLES
    num_columns = 0   # Number of columns detected

    # INPUT VALIDATION
    # tuple_list
    if not isinstance(tuple_list, list):
        raise TypeError(f'The tuple_list argument must of type list instead of {type(tuple_list)}')
    if not tuple_list:
        raise ValueError('The tuple_list argument can not be empty')
    # tuple_list entries
    num_columns = len(tuple_list[0])  # Check all entries against the length of the first
    for entry in tuple_list:
        if not isinstance(entry, tuple):
            raise TypeError(f'Found an invalid tuple_list entry of type {type(entry)}')
        if len(entry) != num_columns:
            raise ValueError('Tuple entries are not a standard length')
    # col_headers
    if not isinstance(col_headers, tuple):
        raise TypeError('The col_headers argument must of type tuple instead of '
                        f'{type(col_headers)}')
    for entry in col_headers:
        if not isinstance(entry, str):
            raise TypeError(f'Found an invalid col_headers entry of type {type(entry)}')
    if len(col_headers) != num_columns:
        raise ValueError('The col_headers argument does not match the length of the tuples')

    # DONE
    return num_columns
