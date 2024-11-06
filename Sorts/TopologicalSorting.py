from collections import defaultdict

"""
A class to represent a directed graph using adjacency list representation.
"""


class Graph:
    def __init__(self):
        """
        Initializes the graph with a default dictionary to store the adjacency list.
        """
        self.graph = defaultdict(list)  # Adjacency list

    def add_edge(self, u, v):
        """
        Adds an edge to the graph.

        Parameters:
        u (int): The starting vertex of the edge.
        v (int): The ending vertex of the edge.
        """

        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        """
        A recursive helper function to perform topological sort.

        Parameters:
        v (int): The current vertex to process.
        visited (set): A set to keep track of visited vertices.
        stack (list): A list to store the topological sort order.
        """

        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, v)  # Push onto the stack

    def topological_sort(self):
        """
        Performs topological sort on the graph and prints the order.

        The function initializes the visited set and stack, then processes each vertex
        to generate the topological sort order.
        """

        visited = set()
        stack = []
        for vertex in list(self.graph):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)
        print("Topological Sort:")
        print(" -> ".join(map(str, stack)))


# Example usage:
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()  # Output: 5 -> 4 -> 2 -> 3 -> 1 -> 0
