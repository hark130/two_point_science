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
from tps.dgraph import create_graph, enumerate_edges, edge_menu
from tps.menu import get_choice, Menu
from tps.tph_constants import TPH_HOSPITAL_LIST
from tps.tph_hospital import TPHHospital


# MACROS
# Menus
MAIN_MENU = Menu('TWO POINT SCIENCE', {1: 'Choose a hospital', 2: 'Graph hospital',
                                       3: 'Print room connections', 999: 'EXIT'})

HOSPITAL_MENU = Menu('TWO POINT HOSPITAL LIST', {i+1: TPH_HOSPITAL_LIST[i] for i in
                                                 range(0, len(TPH_HOSPITAL_LIST))})


def main_menu(sep_rooms: bool) -> None:
    # LOCAL VARIABLES
    user_input = 0       # User menu selection
    hospital_obj = None  # TPH Hospital object for the user-chosen hospital
    max_chances = 3      # Maximum number of invalid inputs tolerated
    clear_screen = True  # Clear the screen before printing a menu
    graph_obj = None     # GraphViz object for hospital's directed graph
    curr_err = ''        # Temp variable which controls error handling
    edge_dict = {}       # Dictionary of rooms and their edge counts
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

        # 1. Choose Hospital
        if 1 == user_input:
            # Hospital chosen by the user
            user_input = get_choice(HOSPITAL_MENU, choice_type=int, clear_screen=clear_screen)
            hospital_obj = TPHHospital(user_input)
            graph_obj = None  # Time to make a new a graphy object
        # 2. Graph Hospital
        elif 2 == user_input:
            if hospital_obj:
                if not graph_obj:
                    graph_obj = create_graph(hospital=hospital_obj, sep_rooms=sep_rooms)
                if graph_obj:
                    print(f'Creating a directed graph of {hospital_obj.get_name()}...')
                    graph_obj.view()
                else:
                    raise RuntimeError('Call to create_graph() failed to return an object')
            else:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
        # 3. Count Edges
        elif 3 == user_input:
            if not hospital_obj:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
            else:
                if not graph_obj:
                    graph_obj = create_graph(hospital=hospital_obj, sep_rooms=sep_rooms)
                    if not graph_obj:
                        raise RuntimeError('Call to create_graph() failed to return an object')
                edge_menu(graph_obj, sep_rooms=sep_rooms)
                clear_screen = False  # I need to see it
                # print(f'SEP ROOMS: {sep_rooms}')  # DEBUGGING
        # 999. Exit
        elif 999 == user_input:
            return
        elif user_input in MAIN_MENU.dictionary.keys():
            raise NotImplementedError(
                f'Menu option {user_input}, "{MAIN_MENU.dictionary[user_input]}", '
                'has not yet been implemented')
        else:
            curr_err = err_template.format('INVALID SELECTION')

        # Is there an error?
        if curr_err:
            max_chances = max_chances - 1
            if max_chances < 1:
                print(err_template.format('TOO MANY INVALID SELECTIONS'))
                return
            else:
                print(curr_err)
                clear_screen = False  # Let them see the mistake they've made
                curr_err = ''


def main() -> None:
    """Constructs and prints a graph for a hospital."""
    # LOCAL VARIABLES
    clear_screen = True                     # Clear the screen before the menu prints
    tps_args = parse_arguments()            # Arguments parsed from sys.argv

    # PARSE ARGS
    # Separate Rooms?
    sep_rooms = separate_rooms(tps_args)

    # MAIN MENU
    main_menu(sep_rooms=sep_rooms)


if __name__ == '__main__':
    main()
