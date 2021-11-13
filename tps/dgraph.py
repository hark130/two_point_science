"""Creates a directed graph on behalf of Two Point Science.

Defines functionality to facilitate the creation of a directed graph based on a give hospital.

    Typical usage example:

    from tps.dgraph import create_graph       # Main functionality
    from tps.tph_hospital import TPHHospital  # Necessary data type
    hospital = TPHHospital('Grockle Bay')     # Create the hospital object
    graph = create_graph(hospital)            # Create the graph object
    graph.view()                              # View the directed graph
"""

# Standard
from typing import Dict

# Third Party
import graphviz

# Local
from tps.tph_constants import TPH_DUAL_PURPOSE_LIST, TPH_ROOM_DICT, TPH_ROOM_LIST
from tps.tph_hospital import TPHHospital
from tps.menu import get_choice, Menu
from tps.misc import print_edge_table


def add_edges(hospital: TPHHospital, graph: graphviz.dot.Digraph,
              sep_rooms: bool = False, focus_node: str = '') -> graphviz.dot.Digraph:
    """Adds edges to graph based on the illnesses found in hospital.

    Args:
        hospital: TPHHospital object. (see: tph_hospital module)
        graph: Graph object to add edges to.
        sep_rooms: Optional; If true, multi-purpose rooms are separated into ' (diag)' and
            ' (treat)' versions on the graph.
        focus_node: Optional; Create a graph based on a specific room instead of the hospital

    Returns:
        graph after edges have been added to it.

    Raises:
        TypeError: Bad data type passed in.
        NotImplementedError: hospital does not contain any illnesses or contains a misconfigured
            illness.
    """
    # LOCAL VARIABLES
    illness_obj_list = []  # List of illness objects from hospital
    temp_diag_list = []    # Temporary list of diag rooms for a given illness
    temp_treat_str = ''    # Temporary treat room for a given illness
    temp_lead_edge = ''    # Temporary leading edge variable
    temp_trail_edge = ''   # Temporary trailing edge variable

    # INPUT VALIDATION
    _validate_add_edges(hospital=hospital, graph=graph, sep_rooms=sep_rooms, focus_node=focus_node)

    # DO IT
    illness_obj_list = hospital.get_illness_objects()
    if not illness_obj_list:
        raise NotImplementedError(f'{hospital.get_name()} is not configured with illnesses')
    for illness_obj in illness_obj_list:
        # Diagnostic room edges
        temp_diag_list = illness_obj.get_diag()
        if temp_diag_list:
            for index in range(0, len(temp_diag_list) - 1):
                temp_lead_edge = temp_diag_list[index]
                temp_trail_edge = temp_diag_list[index + 1]
                graph = _graph_edges(graph=graph, edges=(temp_lead_edge, temp_trail_edge),
                                     sep_rooms=sep_rooms, focus_node=focus_node, all_diag=True)
        else:
            raise NotImplementedError(
                f'{hospital.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a list of diagnostic rooms.')
        # Treatment room edge
        temp_treat_str = illness_obj.get_treat()
        if temp_treat_str:
            temp_lead_edge = temp_diag_list[len(temp_diag_list) - 1]
            temp_trail_edge = temp_treat_str
            graph = _graph_edges(graph=graph, edges=(temp_lead_edge, temp_trail_edge),
                                 sep_rooms=sep_rooms, focus_node=focus_node, all_diag=False)
        else:
            raise NotImplementedError(f'{hospital.get_name()} has an illness, '
                                      f'{illness_obj.get_name()}, missing a treatment room.')

    # DONE
    return graph


def create_graph(hospital: TPHHospital, sep_rooms: bool = False, engine: str = 'dot',
                 graph_format: str = 'png', focus_node: str = '') -> graphviz.dot.Digraph:
    """Create a hospital Digraph using graphviz.

    Args:
        hospital: TPHHospital object. (see: tph_hospital module)
        sep_rooms: Optional; If true, multi-purpose rooms are separated into ' (diag)' and
            ' (treat)' versions on the graph.
        engine: Optional; Digraph build engine: [dot], neato, sfdp, fdp
        graph_format: Optional; File format for Digraph: [png], pdf
        focus_node: Optional; Create a graph based on a specific room instead of the hospital

    Returns:
        Directed graph, complete with room edges, based on hospital.

    Raises:
        TypeError: Bad data type passed in.
        NotImplementedError: hospital does not contain any illnesses or contains a misconfigured
            illness.
    """
    # LOCAL VARIABLES
    graph_obj = None   # graphviz Digraph
    filename = ''      # Filename to save the graph

    # INPUT VALIDATION
    _validate_graph_menu(hospital=hospital, sep_rooms=sep_rooms, engine=engine,
                         graph_format=graph_format)
    # focus_node
    if not isinstance(focus_node, str):
        raise TypeError(f'The focus_node argument must of type str instead of {type(focus_node)}')

    # DO IT
    # Form the filename
    filename = hospital.get_name()
    if focus_node:
        filename = filename + '_' + focus_node
    filename = filename + f' ({engine})'
    # Instantiate the object
    graph_obj = graphviz.Digraph(name=hospital.get_name(), filename=filename,
                                 engine=engine, format=graph_format)
    # Form the nodes/edges
    graph_obj = add_edges(hospital=hospital, graph=graph_obj, sep_rooms=sep_rooms,
                          focus_node=focus_node)

    # DONE
    return graph_obj


# pylint: disable=too-many-branches
def edge_menu(graph: graphviz.dot.Digraph, sep_rooms: bool) -> None:
    """Execute the Two Point Science edge (connection) menu.

    This menu allows the user to print a table with room names, purpose, and an edge (connection)
    count.  The menu also allows the user to sort the table by name or count as well as let the
    user sort the table in ascending or descending order.

    Args:
        graph: Graph object to read the edges from.
        sep_rooms: If true, multi-purpose rooms are separated into ' (diag)' and ' (treat)'
            versions on the table.

    Raises:
        TypeError: Bad data type passed in.
        RuntimeError: Mismatch in internal sort column or sort order variables
    """
    # LOCAL VARIABLES
    sort_col = 'count'    # Print current sort column in the menu title
    sort_by_count = True  # Converts user sort column choice to print_edge_table() kwarg
    sort_dir = 'desc'     # Print current sort direction in the menu title
    sort_desc = True      # Converts user sort order choice to print_edge_table() kwarg
    user_input = 0        # User selection
    edge_dict = None      # Dictionary of room counts
    clear_screen = True   # Clear the screen before printing a menu
    max_chances = 3       # Maximum number of invalid inputs tolerated
    curr_err = ''         # Temp variable which controls error handling
    # Template error message for invalid selections
    err_template = '\n*** ERROR: {}***\n'
    # Template menu title
    menu_title_template = 'EDGE MENU\nSorted by {} in a {} order\n'
    # Menu dictionary
    menu_dict = {1: 'Print room connections', 2: 'Toggle Column', 3: 'Toggle Sort',
                 999: 'Return to main menu'}

    # INPUT VALIDATION
    _validate_edge_menu(graph=graph, sep_rooms=sep_rooms)

    # EDGE MENU
    while True:
        user_input = get_choice(tph_menu=Menu(menu_title_template.format(sort_col, sort_dir),
                                              menu_dict),
                                clear_screen=clear_screen, choice_type=int,
                                max_chances=max_chances, return_choice=True)
        clear_screen = True  # Reset temp variable

        # 1. Print Edges
        if user_input == 1:
            edge_dict = enumerate_edges(graph, sep_rooms)
            print_edge_table(edge_dict, TPH_ROOM_DICT, sort_by_count=sort_by_count,
                             sort_desc=sort_desc)
            clear_screen = False  # Let them see the table
        # 2. Toggle Column
        elif user_input == 2:
            if sort_col == 'count' and sort_by_count:
                sort_col = 'room'
                sort_by_count = False
            elif sort_col == 'room' and not sort_by_count:
                sort_col = 'count'
                sort_by_count = True
            else:
                raise RuntimeError('Mismatch in edge menu sort column toggle settings')
        # 3. Toggle Sort
        elif user_input == 3:
            if sort_dir == 'desc' and sort_desc:
                sort_dir = 'asc'
                sort_desc = False
            elif sort_dir == 'asc' and not sort_desc:
                sort_dir = 'desc'
                sort_desc = True
            else:
                raise RuntimeError('Mismatch in edge menu sort direction toggle settings')
        # 999. Exit
        elif user_input == 999:
            return
        else:
            curr_err = err_template.format('INVALID SELECTION')

        # Is there an error?
        if curr_err:
            max_chances = max_chances - 1
            if max_chances < 1:
                print(err_template.format('TOO MANY INVALID SELECTIONS'))
                return
            print(curr_err)
            clear_screen = False  # Let them see the mistake they've made
            curr_err = ''
# pylint: enable=too-many-branches


# pylint: disable=too-many-branches
def enumerate_edges(graph: graphviz.dot.Digraph, sep_rooms: bool) -> Dict[str, int]:
    """Execute the Two Point Science edge (connection) menu.

    This menu allows the user to print a table with room names, purpose, and an edge (connection)
    count.  The menu also allows the user to sort the table by name or count as well as let the
    user sort the table in ascending or descending order.

    Args:
        graph: Graph object to read the edges from.
        sep_rooms: If true, multi-purpose rooms are separated into ' (diag)' and ' (treat)'
            versions on the table.

    Raises:
        TypeError: Bad data type passed in.
        RuntimeError: Mismatch in internal sort column or sort order variables
    """
    # LOCAL VARIABLES
    edge_counts = {}      # Rooms: Room Count
    temp_room_names = []  # Temporary variable to help resolve dual use rooms

    # INPUT VALIDATION
    # graph
    if not isinstance(graph, graphviz.dot.Digraph):
        raise TypeError(f'The graph can not be of type {type(graph)}')
    # sep_rooms
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms argument must of type bool instead of {type(sep_rooms)}')

    # ENUMERATE IT
    for part in graph.body:
        for room in TPH_ROOM_LIST:
            if room in part:
                # List of room names to look for
                if sep_rooms and TPH_ROOM_DICT[room].purpose == 'Both':
                    temp_room_names.append(room + ' (diag)')
                    temp_room_names.append(room + ' (treat)')
                else:
                    temp_room_names.append(room)
                # Look for the room names
                for temp_room_name in temp_room_names:
                    if temp_room_name in edge_counts.keys():
                        edge_counts[temp_room_name] = edge_counts[temp_room_name] + 1
                    else:
                        edge_counts[temp_room_name] = 1
                # print(f'TEMP ROOM NAMES {temp_room_names}')
                # Clear temp variables
                temp_room_names = []

    # VALIDATE RESULTS
    for key, value in edge_counts.items():
        if not isinstance(key, str):
            raise TypeError('Invalid key type detected')
        if not isinstance(value, int):
            raise TypeError('Invalid value type detected')

    # DONE
    return edge_counts
# pylint: enable=too-many-branches


def room_menu(hospital: TPHHospital, sep_rooms: bool = False, engine: str = 'dot',
              graph_format: str = 'png') -> None:
    """Execute the Two Point Science room menu.

    Prompts the user for a room associated with hospital and then creates a graph of all edges
    associate with that room.

    Args:
        hospital: TPHHospital object. (see: tph_hospital module)
        sep_rooms: Optional; If true, multi-purpose rooms are separated into ' (diag)' and
            ' (treat)' versions on the graph.
        engine: Optional; Digraph build engine: [dot], neato, sfdp, fdp
        graph_format: Optional; File format for Digraph: [png], pdf

    Raises:
        TypeError: Bad data type passed in.
    """
    # LOCAL VARIABLES
    user_choice = ''        # User's room name selection
    local_room_menu = None  # Menu object for get_choice()
    new_dict = {}           # Create a dictionary based on hospital room list
    graph_obj = None        # graphviz.dot.Digraph returned by create_graph()
    room_list = []          # List of all the rooms in hospital

    # INPUT VALIDATION
    _validate_graph_menu(hospital=hospital, sep_rooms=sep_rooms, engine=engine,
                         graph_format=graph_format)

    # GET ROOM
    # Trim the dictionary
    room_list = hospital.get_room_list(sort_list=True)
    new_dict = {i+1: room_list[i] for i in range(0, len(room_list))}
    # Separate rooms
    if sep_rooms:
        new_dict = _create_sep_room_dict(new_dict)
    local_room_menu = Menu(hospital.get_name().upper() + 'ROOM LIST', new_dict)
    # Get user input
    user_choice = get_choice(local_room_menu, clear_screen=True, choice_type=int)

    # MAKE GRAPH
    graph_obj = create_graph(hospital=hospital, sep_rooms=sep_rooms, engine=engine,
                             graph_format=graph_format, focus_node=user_choice)
    print(f"Creating a directed graph of {hospital.get_name()}'s {user_choice} room...")
    graph_obj.view()


def _create_sep_room_dict(room_dict: dict) -> Dict[int, str]:
    # LOCAL VARIABLES
    new_dict = {}  # Return value
    index = 1      # New indices for the new dictionary

    # INPUT VALIDATION
    if not isinstance(room_dict, dict):
        raise TypeError(f'The room_dict argument must of type dict instead of {type(room_dict)}')

    # DO IT
    for _, room_name in room_dict.items():
        try:
            if TPH_ROOM_DICT[room_name].purpose == 'Both':
                new_dict[index] = room_name + ' (diag)'
                index = index + 1
                new_dict[index] = room_name + ' (treat)'
            else:
                new_dict[index] = room_name
        except AttributeError:
            pass  # <shrug>
        else:
            index = index + 1

    # DONE
    return new_dict


def _graph_edges(graph: graphviz.dot.Digraph, edges: tuple,
                 sep_rooms: bool, focus_node: str, all_diag: bool) -> graphviz.dot.Digraph:
    """Adds edges to graph in a particular way on behalf of add_edges().

    WARNING: Does not validate input!

    A lot of assumptions are made in this function.  Most importantly are use cases:
        (1) diag -> diag and (2) diag -> treat.  If all_diag is True, use case (1) is used.
        Otherwise, (2).
    """
    # LOCAL VARIABLES
    temp_lead_edge = edges[0]   # We might need to modify the leading edge
    temp_trail_edge = edges[1]  # We might need to modify the trailing edge
    diag_suffix = ' (diag)'     # If dual-use rooms are separate, diagnostic suffix
    treat_suffix = ' (treat)'   # If dual-use rooms are separate, treatment suffix
    trail_suffix = ''           # Determined by all_diag

    # DO IT (and don't ask questions)
    # Determine trailing suffix
    if all_diag:
        trail_suffix = diag_suffix
    else:
        trail_suffix = treat_suffix
    # Graph the edge
    if sep_rooms and temp_lead_edge in TPH_DUAL_PURPOSE_LIST:
        temp_lead_edge = temp_lead_edge + diag_suffix
    if sep_rooms and temp_trail_edge in TPH_DUAL_PURPOSE_LIST:
        temp_trail_edge = temp_trail_edge + trail_suffix
    if focus_node:
        if focus_node in (temp_lead_edge, temp_trail_edge):
            graph.edge(temp_lead_edge, temp_trail_edge)
    else:
        graph.edge(temp_lead_edge, temp_trail_edge)

    # DONE
    return graph


def _validate_add_edges(hospital: TPHHospital, graph: graphviz.dot.Digraph,
                        sep_rooms: bool, focus_node: str) -> None:
    """Validate input on behalf of add_edges()."""
    # INPUT VALIDATION
    # hospital
    if not isinstance(hospital, TPHHospital):
        raise TypeError(f'The hospital can not be of type {type(hospital)}')
    illness_obj_list = hospital.get_illness_objects()
    if not illness_obj_list:
        raise NotImplementedError(f'{hospital.get_name()} does not appear to be defined')
    # graph
    if not isinstance(graph, graphviz.dot.Digraph):
        raise TypeError(f'The graph can not be of type {type(graph)}')
    # sep_rooms
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms can not be of type {type(sep_rooms)}')
    # focus_node
    if not isinstance(focus_node, str):
        raise TypeError(f'The focus_node argument must of type str instead of {type(focus_node)}')


def _validate_edge_menu(graph: graphviz.dot.Digraph, sep_rooms: bool) -> None:
    """Validate input on behalf of edge_menu()."""
    # INPUT VALIDATION
    # graph
    if not isinstance(graph, graphviz.dot.Digraph):
        raise TypeError(f'The graph can not be of type {type(graph)}')
    # sep_rooms
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms argument must of type bool instead of {type(sep_rooms)}')


def _validate_graph_menu(hospital: TPHHospital, sep_rooms: bool, engine: str,
                         graph_format: str) -> None:
    """Validate input on behalf of functions that create graphs."""
    # INPUT VALIDATION
    # hospital
    if not isinstance(hospital, TPHHospital):
        raise TypeError(f'The hospital can not be of type {type(hospital)}')
    # sep_rooms
    if not isinstance(sep_rooms, bool):
        raise TypeError(f'The sep_rooms can not be of type {type(sep_rooms)}')
    # engine
    if not isinstance(engine, str):
        raise TypeError(f'The engine can not be of type {type(engine)}')
    # graph_format
    if not isinstance(graph_format, str):
        raise TypeError(f'The graph_format can not be of type {type(graph_format)}')
