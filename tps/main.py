"""Defines the Two Point Science package entry point.

Defines main() which will construct and print a graphy for one Two Point Hospital hospital.

    Typical usage example:

    from tps.tph_main import main
    main()
"""

# Standard
import sys

# Third Party
import graphviz as gv

# Local
from tps.arguments import parse_arguments, separate_rooms
from tps.dgraph import create_graph
from tps.menu import get_choice
from tps.tph_constants import HOSPITAL_MENU
from tps.tph_hospital import TPHHospital


def main() -> None:
    """Constructs and prints a graph for a hospital."""
    # LOCAL VARIABLES
    clear_screen = True                     # Clear the screen before the menu prints
    tps_args = parse_arguments()            # Arguments parsed from sys.argv
    # Hospital chosen by the user
    user_input = get_choice(HOSPITAL_MENU, choice_type=int, clear_screen=clear_screen)
    engine = 'dot'                          # Engine used by graphviz
    hospital_obj = TPHHospital(user_input)  # The TPH Hospital object
    temp_diag_list = []                     # Temporary list of diag rooms for a given illness
    temp_treat_str = ''                     # Temporary treat room for a given illness
    graph_obj = None                        # GraphViz object for hospital's directed graph

    # DO IT
    # Separate Rooms?
    sep_rooms = separate_rooms(tps_args)
    # Form Graph
    graph_obj = create_graph(hospital=hospital_obj, sep_rooms=sep_rooms)

    # DONE
    if graph_obj:
        print(f'Creating a directed graph of {hospital_obj.get_name()}...')
        graph_obj.view()
    else:
        raise RuntimeError('Call to create_graph() failed to return an object')


if __name__ == '__main__':
    main()
