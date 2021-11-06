# Standard
# Third Party
# import matplotlib.pyplot as plt
# import networkx as nx
import graphviz as gv
# Local
from tps.tph_hospital import TPHHospital

# CURR_HOSPITAL = 'Blighton'  # Placeholder for user input
# CURR_HOSPITAL = 'Smogley'  # Placeholder for user input
CURR_HOSPITAL = 'Grockle Bay'  # Placeholder for user input


def main() -> None:
    # LOCAL VARIABLES
    user_input = CURR_HOSPITAL              # Hard-coded in lieu of menu feature
    hospital_obj = TPHHospital(user_input)  # The TPH Hospital object
    # graph_obj = gv.Digraph('G', filename='test_none')  # Default is dot
    graph_obj = gv.Digraph(name=CURR_HOSPITAL, filename=CURR_HOSPITAL+' (dot)', engine='dot',
                           format='png')  # This is ok; Good arrangement
    # graph_obj = gv.Graph(name=CURR_HOSPITAL, filename=CURR_HOSPITAL+' (dot)', engine='dot',
    #                      format='png')  # Not as good... no arrows
    # graph_obj = gv.Digraph('G', filename='test_neato', engine='neato')  # Cluttered but useable
    # graph_obj = gv.Digraph('G', filename='test_sfdp', engine='sfdp')  # Busy and small
    # graph_obj = gv.Digraph('G', filename='test_fdp', engine='fdp')  # Busy
    temp_diag_list = []                     # Temporary list of diag rooms for a given illness
    temp_treat_str = ''                     # Temporary treat room for a given illness

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
    graph_obj.view()


if __name__ == '__main__':
    main()
