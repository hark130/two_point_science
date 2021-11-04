# Standard
# Third Party
import matplotlib.pyplot as plt
import networkx as nx
# Local
from tps.tph_hospital import TPHHospital


def main() -> None:
    # LOCAL VARIABLES
    user_input = 'Grockle Bay'              # Hard-coded in lieu of menu feature
    hospital_obj = TPHHospital(user_input)  # The TPH Hospital object
    # graph_obj = nx.Graph()                  # Networkx Graph object (Doesn't do bi-directional arrows)
    # graph_obj = nx.DiGraph()                # Networkx DiGraph object
    # graph_obj = nx.MultiGraph()             # Networkx MultiGraph object
    graph_obj = nx.MultiDiGraph()           # Networkx MultiDiGraph object draws bi-directional arrows (CURRENT FAV)
    # graph_obj = nx.OrderedDiGraph()         # Networkx OrderedDiGraph object draws arrows
    # graph_obj = nx.dodecahedral_graph()     # From the help (Don't like the extra graph)
    temp_diag_list = []                     # Temporary list of diag rooms for a given illness
    temp_treat_str = ''                     # Temporary treat room for a given illness

    # print(f'{user_input} Illness Names: {hospital_obj.get_illness_names()}')  # DEBUGGING
    # print(f'{user_input} Illness Objects: {hospital_obj.get_illness_objects()}')  # DEBUGGING

    # DO IT
    # Form Graph
    print(f'NUMBER OF NODES: {graph_obj.number_of_nodes()}')  # DEBUGGING
    for illness_obj in hospital_obj.get_illness_objects():
        # Diagnostic room edges
        temp_diag_list = illness_obj.get_diag()
        if temp_diag_list:
            for index in range(0, len(temp_diag_list) - 1):
                graph_obj.add_edge(temp_diag_list[index], temp_diag_list[index + 1])
        else:
            raise NotImplementedError(f'{hospital_obj.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a list of diagnostic rooms.')
        # Treatment room edge
        temp_treat_str = illness_obj.get_treat()
        if temp_treat_str:
            graph_obj.add_edge(temp_diag_list[len(temp_diag_list) - 1], temp_treat_str)
        else:
            print(hospital_obj.get_name())
            print(illness_obj.get_name())
            raise NotImplementedError(f'{hospital_obj.get_name()} has an illness, '
                f'{illness_obj.get_name()}, missing a treatment room.')

    print(f'NUMBER OF NODES: {graph_obj.number_of_nodes()}')  # DEBUGGING
    # Print Graph
    # nx.draw(graph_obj, with_labels=True)
    # nx.draw(graph_obj, pos=nx.spring_layout(graph_obj), with_labels=True)  # use spring layout
    nx.draw(graph_obj, arrows=True, arrowsize=20, with_labels=True, node_shape='8', node_size=900)
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
    plt.show()

if __name__ == '__main__':
    main()
