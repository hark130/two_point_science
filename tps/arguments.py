"""Defines and parses Two Point Science package arguments.

Functionality parses arguments and answers questions about defined arguments: -d/--distinct-rooms

    Typical usage example:

    from tps.arguments import parse_arguments, separate_rooms
    args = parse_arguments()
    if separate_rooms(args):
        print('User requires we separate dual-purpose rooms in the directed graph')
    else:
        print('User wants dual-purpose rooms to do dual-duty on the directed graph')
"""

# Standard
import argparse

# Third Party

# Local


def parse_arguments() -> argparse.Namespace:
    """Parse the arguments on behalf of Two Point Science."""
    parser = argparse.ArgumentParser(
        description='Create a directed graph of rooms for a Two Point Hospital hospital')
    parser.add_argument('-d', '--distinct-rooms', action='store_true', default=False,
                        help='Separate dual-purpose rooms on the directed graph')
    args = parser.parse_args()

    # DONE
    return args


def separate_rooms(args: argparse.Namespace) -> bool:
    """Determine if rooms should be separated."""
    # LOCAL VARIABLES
    separate = False  # Argument is found and True

    # INPUT VALIDATION
    if not isinstance(args, argparse.Namespace):
        raise TypeError(f'The args parameter can not be of type {type(args)}')

    # CHECK IT
    try:
        if args.distinct_rooms:
            separate = True
    except AttributeError:
        pass

    # DONE
    return separate
