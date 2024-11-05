class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # Default dictionary to store graph

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])  # Edge from u to v with weight w

    # Find function for union-find
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    # Union function for union-find
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            # Ranks are same, make one as root and increment its rank by one
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []  # Store the resultant MST
        i, e = 0, 0  # Indices for sorted edges and result[]

        # Step 1: Sort all edges in non-decreasing order of weight
        self.graph.sort(key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is V-1
        while e < self.V - 1:
            # Pick the smallest edge and increment index
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause cycle
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the constructed MST
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")


# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
