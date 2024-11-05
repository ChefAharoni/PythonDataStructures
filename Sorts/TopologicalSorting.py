from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
        stack.insert(0, v)  # Push onto the stack

    def topological_sort(self):
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
