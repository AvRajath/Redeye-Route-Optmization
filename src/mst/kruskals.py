<<<<<<< HEAD
import sys

=======
>>>>>>> 0dd6f85 (added graph formationcode)
class MST:
    parent = []
    def __init__(self, num_vertices):
        self.parent = [i for i in range(num_vertices)]
        pass

    # finds the parent of a vertex
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    # union of two sets
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[xroot] = yroot

    # Kruskal's algorithm
    def kruskalMST(self, adj_matrix):
        mincost = 0  # Cost of min MST
        num_vertices = len(self.parent)
        # Initialize sets of disjoint sets
        for i in range(num_vertices):
            self.parent[i] = i

        # Include minimum weight edges one by one
        edge_count = 0
        while edge_count < num_vertices - 1:
            min = sys.maxsize
            a = -1
            b = -1
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if self.find(i) != self.find(j) and adj_matrix[i][j] < min:
                        min = adj_matrix[i][j]
                        a = i
                        b = j
            self.union(a, b)
            print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
            edge_count += 1
            mincost += min

        print("Minimum cost= {}".format(mincost))


# example graph represented by an adjacency matrix
# graph = [[0, 2, 7, 6, 3],
#          [2, 0, 3, 8, 5],
#          [1, 3, 0, 2, 7],
#          [6, 8, 1, 0, 9],
#          [1, 5, 7, 9, 0]]
#
# # find the minimum spanning tree using Kruskal's algorithm
# # kruskalMST(graph)
#
# mst = MST(5)
# mst.kruskalMST(graph)