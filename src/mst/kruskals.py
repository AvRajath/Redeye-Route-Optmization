class RouteGraph:
    adj_matrix = []
    location_map = {}

    def __init__(self):
        pass

    def add_locations(self):
        pass

    def add_time_distance(self, location1, location2):
        pass


class MST:

    def __init__(self):
        pass

    # finds the parent of a vertex
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    # union of two sets
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    # Kruskal's algorithm
    def kruskalMST(self, graph):
        result = []  # to store the result
        i = 0  # index variable for sorted edges
        e = 0  # index variable for result[]

        # get the number of vertices in the graph
        V = len(graph)

        # create an empty list to store the parents of each vertex
        parent = []

        # create an empty list to store the rank of each vertex
        rank = []

        # initialize the parent and rank lists
        for node in range(V):
            parent.append(node)
            rank.append(0)

        # sort the edges of the graph in ascending order of weight
        sorted_edges = sorted(range(len(graph)), key=lambda i: graph[i])
        print(sorted_edges)
        # loop through all the edges of the graph
        while e < V - 1:

            # get the next smallest edge
            u, v, w = sorted_edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if adding the edge doesn't create a cycle, add it to the result
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # print the MST
        print("Edges of the Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")



# example graph represented by an adjacency matrix
graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

# find the minimum spanning tree using Kruskal's algorithm
# kruskalMST(graph)

mst = MST()
mst.kruskalMST(graph)