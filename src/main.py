import graph
from mst import kruskals
from helper import constants
import pprint

def main():

    route_graph = graph.RouteGraph(constants.Constants.XLSPATH.value)
    adj_mat_dist = route_graph.form_adjacency_matrix_distance()
    # adj_mat_time = route_graph.form_adjacency_matrix_time()
    pprint.pprint(adj_mat_dist)

    mst_obj = kruskals.MST(len(adj_mat_dist[0]))
    mst_obj.kruskalMST(adj_mat_dist)
    pass

if __name__ == "__main__":
    main()