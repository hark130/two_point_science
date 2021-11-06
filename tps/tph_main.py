# Standard
# Third Party
import matplotlib.pyplot as plt
import networkx as nx
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
    # graph_obj = nx.Graph()                  # Networkx Graph object (Doesn't do bi-directional arrows)
    # graph_obj = nx.DiGraph()                # Networkx DiGraph object
    # graph_obj = nx.MultiGraph()             # Networkx MultiGraph object
    # graph_obj = nx.MultiDiGraph()           # Networkx MultiDiGraph object draws bi-directional arrows (CURRENT FAV)
    # graph_obj = gv.Digraph('G', filename='test_none')  # Default is dot
    graph_obj = gv.Digraph(name=CURR_HOSPITAL, filename=CURR_HOSPITAL+' (dot)', engine='dot', format='png')  # This is ok; Good arrangement
    # graph_obj = gv.Digraph('G', filename='test_neato', engine='neato')  # Cluttered but consider this for smaller graphs
    # graph_obj = gv.Digraph('G', filename='test_sfdp', engine='sfdp')  # Busy and small
    # graph_obj = gv.Digraph('G', filename='test_fdp', engine='fdp')  # Busy
    # graph_obj = nx.OrderedDiGraph()         # Networkx OrderedDiGraph object draws arrows
    # graph_obj = nx.dodecahedral_graph()     # From the help (Don't like the extra graph)
    temp_diag_list = []                     # Temporary list of diag rooms for a given illness
    temp_treat_str = ''                     # Temporary treat room for a given illness

    # print(f'{user_input} Illness Names: {hospital_obj.get_illness_names()}')  # DEBUGGING
    # print(f'{user_input} Illness Objects: {hospital_obj.get_illness_objects()}')  # DEBUGGING

    # DO IT
    # Form Graph
    # print(f'NUMBER OF NODES: {graph_obj.number_of_nodes()}')  # DEBUGGING
    for illness_obj in hospital_obj.get_illness_objects():
        # Diagnostic room edges
        temp_diag_list = illness_obj.get_diag()
        if temp_diag_list:
            for index in range(0, len(temp_diag_list) - 1):
                # graph_obj.add_edge(temp_diag_list[index], temp_diag_list[index + 1])  # nx
                graph_obj.edge(temp_diag_list[index], temp_diag_list[index + 1])  # gv
                # graph_obj.edge(temp_diag_list[index], temp_diag_list[index + 1], label=illness_obj.get_name())  # gv
        else:
            raise NotImplementedError(f'{hospital_obj.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a list of diagnostic rooms.')
        # Treatment room edge
        temp_treat_str = illness_obj.get_treat()
        if temp_treat_str:
            # graph_obj.add_edge(temp_diag_list[len(temp_diag_list) - 1], temp_treat_str)  # nx
            graph_obj.edge(temp_diag_list[len(temp_diag_list) - 1], temp_treat_str)  # gv
            # graph_obj.edge(temp_diag_list[len(temp_diag_list) - 1], temp_treat_str, label=illness_obj.get_name())  # gv
        else:
            # print(hospital_obj.get_name())  # DEBUGGING
            # print(illness_obj.get_name())  # DEBUGGING
            raise NotImplementedError(f'{hospital_obj.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a treatment room.')

    ##############################################################################################
    ########################################## NETWORKX ##########################################
    ##############################################################################################

    # print(f'NUMBER OF NODES: {graph_obj.number_of_nodes()}')  # DEBUGGING
    # Print Graph
    ##############################################################################################
    # import networkx as nx
    # help(nx.draw_networkx)  # For options
    # OPTIONS:
    # node_shape - The shape of the node.  Specification is as matplotlib.scatter
    #   marker, one of 'so^>v<dph8'.
    # https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
    #   s - Square
    #   o - Circle
    #   ^ - Triangle (up)
    #   > - Triangle (right)
    #   v - Triangle (down)
    #   < - Triangle (left)
    #   d - Thin Diamond
    #   p - Plus (filled)
    #   h - Hexagon1
    #   8 - Octagon
    ##############################################################################################

    ##############################################################################################
    # import networkx as nx
    # help(nx.drawing.layout)
    # FUNCTIONS
    # bipartite_layout  # Nodes are in a straight line... do not like
    # circular_layout  # I kinda like this
    # fruchterman_reingold_layout  # This is the layout that made me look for a better layout
    # kamada_kawai_layout  # Better distribution of nodes, facilitates intuitive interpretation
    # multipartite_layout  # Needs a subset_key
    # planar_layout  # Apparently, my graph is not planar
    # random_layout  # Tough to read; Even if this layout is useful, it's not useful here
    # rescale_layout  # Needs a shape attribute
    # shell_layout  # A better version of the circle; More intuitive than circle but not as much as kamada
    # spectral_layout  # Zero use here
    # spiral_layout  # Not as good as circle but better than random
    # spring_layout  # Tough to read; This is the layout that made me look for a better layout
    #
    # FINALISTS
    # kamada_kawai_layout  # Better distribution of nodes, facilitates intuitive interpretation
    # shell_layout  # A better version of the circle; More intuitive than circle but not as much as kamada
    #
    ##############################################################################################
    # graph_obj = nx.MultiDiGraph()           # Networkx MultiDiGraph object draws bi-directional arrows (CURRENT FAV)
    # nx.draw(graph_obj, pos=nx.kamada_kawai_layout(graph_obj), arrows=True, arrowsize=20, with_labels=True, node_shape='8', node_size=900)  # nx
    # nx.draw(graph_obj, pos=nx.kamada_kawai_layout(graph_obj), arrows=True, arrowsize=20, with_labels=True, node_shape='8', node_size=900)  # gv
    # plt.show()

    ##############################################################################################
    ########################################## GRAPHVIZ ##########################################
    ##############################################################################################
    graph_obj.view()

    # DONE

if __name__ == '__main__':
    main()
