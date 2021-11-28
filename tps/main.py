"""Defines the Two Point Science package entry point.

Defines main() which will construct and print a graphy for one Two Point Hospital hospital.

    Typical usage example:

    from tps.tph_main import main
    main()
"""

# Standard

# Third Party

# Local
from tps.arguments import parse_arguments, graph_directory, separate_rooms
from tps.dgraph import create_graph, edge_menu, illness_menu, room_menu
from tps.menu import _check_for_error, danger_menu, get_choice, Menu
from tps.tph_constants import TPH_HOSPITAL_LIST
from tps.tph_hospital import TPHHospital


# MACROS
# Menus
MAIN_MENU = Menu('TWO POINT SCIENCE', {1: 'Choose a hospital', 2: 'Graph hospital',
                                       3: 'Graph illness', 4: 'Graph room',
                                       5: 'Print room connections', 6: 'Print illness danger',
                                       999: 'EXIT'})

HOSPITAL_MENU = Menu('TWO POINT HOSPITAL LIST', {i+1: TPH_HOSPITAL_LIST[i] for i in
                                                 range(0, len(TPH_HOSPITAL_LIST))})


# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
def main_menu(sep_rooms: bool, graph_dir: str) -> None:
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
    # sep_rooms
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms argument must of type bool instead of {type(sep_rooms)}')
    # graph_dir
    if not isinstance(graph_dir, str):
        raise TypeError(f'The graph_dir argument must of type str instead of {type(graph_dir)}')

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
                graph_obj = create_graph(hospital=hospital_obj, graph_dir=graph_dir,
                                         sep_rooms=sep_rooms)
                print(f'Creating a directed graph of {hospital_obj.get_name()}...')
                graph_obj.view()
            else:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
        # 3. Graph Illness
        elif user_input == 3:
            if hospital_obj:
                illness_menu(hospital=hospital_obj, graph_dir=graph_dir, sep_rooms=sep_rooms)
            else:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
        # 4. Graph Room
        elif user_input == 4:
            if hospital_obj:
                room_menu(hospital=hospital_obj, graph_dir=graph_dir, sep_rooms=sep_rooms)
            else:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
        # 5. Count Edges
        elif user_input == 5:
            if not hospital_obj:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
            else:
                graph_obj = create_graph(hospital=hospital_obj, graph_dir=graph_dir,
                                         sep_rooms=sep_rooms)
                edge_menu(graph_obj, sep_rooms=sep_rooms)
                clear_screen = False  # User needs to see it
        # 6. Calculate Danger
        elif user_input == 6:
            if not hospital_obj:
                curr_err = err_template.format('CHOOSE A HOSPITAL')
            else:
                danger_menu(hospital=hospital_obj)
                clear_screen = False  # User needs to see it
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
            print(err_template.format(err.args[0]))
            return
# pylint: enable=too-many-branches
# pylint: enable=too-many-statements


def main() -> None:
    """Constructs and prints a graph for a hospital."""
    # LOCAL VARIABLES
    tps_args = parse_arguments()  # Arguments parsed from sys.argv
    # Separate Rooms?
    sep_rooms = separate_rooms(tps_args)
    # Directory to store the graph files in
    graph_dir = graph_directory(tps_args)

    # MAIN MENU
    main_menu(sep_rooms=sep_rooms, graph_dir=graph_dir)


if __name__ == '__main__':
    main()
