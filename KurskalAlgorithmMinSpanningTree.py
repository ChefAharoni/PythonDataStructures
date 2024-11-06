class Graph:
    """
    A class to represent a graph using an edge list representation.

    Attributes:
    -----------
    V : int
        Number of vertices in the graph.
    graph : list
        List to store the graph edges in the form [u, v, w] where u and v are vertices and w is the weight of the edge.
    """

    def __init__(self, vertices):
        """
        Constructs all the necessary attributes for the graph object.

        Parameters:
        -----------
        vertices : int
            Number of vertices in the graph.
        """
        self.V = vertices  # Number of vertices
        self.graph = []  # Default dictionary to store graph

    def add_edge(self, u, v, w):
        """
        Adds an edge to the graph.

        Parameters:
        -----------
        u : int
            The starting vertex of the edge.
        v : int
            The ending vertex of the edge.
        w : int
            The weight of the edge.
        """
        self.graph.append([u, v, w])  # Edge from u to v with weight w

    # Find function for union-find
    def find(self, parent, i):
        """
        A function to find the set of an element i using path compression.

        Parameters:
        -----------
        parent : list
            The parent list where parent[i] is the parent of i.
        i : int
            The element to find the set of.

        Returns:
        --------
        int
            The representative of the set containing i.
        """
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    # Union function for union-find
    def union(self, parent, rank, x, y):
        """
        A function that does union of two sets of x and y using union by rank.

        Parameters:
        -----------
        parent : list
            The parent list where parent[i] is the parent of i.
        rank : list
            The rank list where rank[i] is the rank of the set containing i.
        x : int
            The first element.
        y : int
            The second element.
        """
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
        """
        Function to construct and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
        The function follows these steps:
        1. Sort all the edges in non-decreasing order of their weight.
        2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
           If cycle is not formed, include this edge. Else, discard it.
        3. Repeat step 2 until there are (V-1) edges in the spanning tree.

        Prints:
        -------
        The edges in the constructed MST and their weights.
        """
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
