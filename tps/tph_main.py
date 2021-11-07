"""Defines the Two Point Science package entry point.

Defines main() which will construct and print a graphy for one Two Point Hospital hospital.

    Typical usage example:

    from tps.tph_main import main
    main()
"""

# Standard

# Third Party
# import matplotlib.pyplot as plt
# import networkx as nx
import graphviz as gv

# Local
from tps.tph_constants import HOSPITAL_MENU
from tps.tph_hospital import TPHHospital
from tps.tph_menu import get_choice

# CURR_HOSPITAL = 'Blighton'  # Placeholder for user input
# CURR_HOSPITAL = 'Smogley'  # Placeholder for user input
CURR_HOSPITAL = 'Grockle Bay'  # Placeholder for user input


def main() -> None:
    """Constructs and prints a graph for a hospital."""
    # LOCAL VARIABLES
    user_input = get_choice(HOSPITAL_MENU)  # Hard-coded in lieu of menu feature
    engine = 'dot'                          # Engine used by graphviz
    hospital_obj = TPHHospital(user_input)  # The TPH Hospital object
    temp_diag_list = []                     # Temporary list of diag rooms for a given illness
    temp_treat_str = ''                     # Temporary treat room for a given illness
    # GraphViz object used to create the directed graph of the user's chosen hospital
    graph_obj = gv.Digraph(name=hospital_obj.get_name(),
                           filename=hospital_obj.get_name()+f' ({engine})',
                           engine=engine, format='png')

    # DO IT
    # Form Graph
    for illness_obj in hospital_obj.get_illness_objects():
        # Diagnostic room edges
        temp_diag_list = illness_obj.get_diag()
        if temp_diag_list:
            for index in range(0, len(temp_diag_list) - 1):
                graph_obj.edge(temp_diag_list[index], temp_diag_list[index + 1])  # gv
        else:
            raise NotImplementedError(
                f'{hospital_obj.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a list of diagnostic rooms.')
        # Treatment room edge
        temp_treat_str = illness_obj.get_treat()
        if temp_treat_str:
            graph_obj.edge(temp_diag_list[len(temp_diag_list) - 1], temp_treat_str)  # gv
        else:
            raise NotImplementedError(f'{hospital_obj.get_name()} has an illness, '
                                      f'{illness_obj.get_name()}, missing a treatment room.')

    # DONE
    print(f'Creating a directed graphy of {hospital_obj.get_name()}')
    graph_obj.view()


if __name__ == '__main__':
    main()
