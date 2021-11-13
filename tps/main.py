"""Defines the Two Point Science package entry point.

Defines main() which will construct and print a graphy for one Two Point Hospital hospital.

    Typical usage example:

    from tps.tph_main import main
    main()
"""

# Standard

# Third Party

# Local
from tps.arguments import parse_arguments, separate_rooms
from tps.dgraph import create_graph, edge_menu
from tps.menu import _check_for_error, get_choice, Menu
from tps.tph_constants import TPH_HOSPITAL_LIST
from tps.tph_hospital import TPHHospital


# MACROS
# Menus
MAIN_MENU = Menu('TWO POINT SCIENCE', {1: 'Choose a hospital', 2: 'Graph hospital',
                                       3: 'Print room connections', 999: 'EXIT'})

HOSPITAL_MENU = Menu('TWO POINT HOSPITAL LIST', {i+1: TPH_HOSPITAL_LIST[i] for i in
                                                 range(0, len(TPH_HOSPITAL_LIST))})


# pylint: disable=too-many-branches
def main_menu(sep_rooms: bool) -> None:
    """Execute the Two Point Science top-level menu.

    Args:
        sep_rooms: If true, multi-purpose rooms are separated into ' (diag)' and ' (treat)'
            versions for user output.

    Raises:
        TypeError: Bad data type passed in.
    """
    # LOCAL VARIABLES
    user_input = 0       # User menu selection
    hospital_obj = None  # TPH Hospital object for the user-chosen hospital
    max_chances = 3      # Maximum number of invalid inputs tolerated
    clear_screen = True  # Clear the screen before printing a menu
    graph_obj = None     # GraphViz object for hospital's directed graph
    curr_err = ''        # Temp variable which controls error handling
    # Template error message for invalid selections
    err_template = '\n*** ERROR: {}***\n'

    # INPUT VALIDATION
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms argument must of type bool instead of {type(sep_rooms)}')

    # DO IT
    while True:
        user_input = get_choice(MAIN_MENU, clear_screen=clear_screen, choice_type=int,
                                max_chances=max_chances, return_choice=True)
        clear_screen = True  # Reset temp variable
        curr_err = ''  # Reset temp variable

        # 1. Choose Hospital
        if user_input == 1:
            # Hospital chosen by the user
            user_input = get_choice(HOSPITAL_MENU, choice_type=int, clear_screen=clear_screen)
            hospital_obj = TPHHospital(user_input)
            graph_obj = None  # Time to make a new a graphy object
        # 2. Graph Hospital
        elif user_input == 2:
            if hospital_obj:
                graph_obj = create_graph(hospital=hospital_obj, sep_rooms=sep_rooms)
                print(f'Creating a directed graph of {hospital_obj.get_name()}...')
                graph_obj.view()
            else:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
        # 3. Count Edges
        elif user_input == 3:
            if not hospital_obj:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
            else:
                graph_obj = create_graph(hospital=hospital_obj, sep_rooms=sep_rooms)
                edge_menu(graph_obj, sep_rooms=sep_rooms)
                clear_screen = False  # I need to see it
                # print(f'SEP ROOMS: {sep_rooms}')  # DEBUGGING
        # 999. Exit
        elif user_input == 999:
            return
        else:
            curr_err = err_template.format('INVALID SELECTION')

        # Is there an error?
        try:
            max_chances, clear_screen = _check_for_error(curr_err=curr_err,
                                                         max_chances=max_chances)
        except RuntimeWarning as err:
            print(f'EXCEPTION {repr(err)}')  # DEBUGGING
            print(err_template.format(err.args[0]))
            return
# pylint: enable=too-many-branches


def main() -> None:
    """Constructs and prints a graph for a hospital."""
    # LOCAL VARIABLES
    tps_args = parse_arguments()  # Arguments parsed from sys.argv

    # PARSE ARGS
    # Separate Rooms?
    sep_rooms = separate_rooms(tps_args)

    # MAIN MENU
    main_menu(sep_rooms=sep_rooms)


if __name__ == '__main__':
    main()
