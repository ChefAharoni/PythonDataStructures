from collections import deque


def bfs(graph, start):
    """
    Perform a breadth-first search (BFS) on a graph starting from a given node.
    Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are the nodes, and the values are lists of neighboring nodes.
        start: The starting node for the BFS traversal.
    Returns:
        None: This function prints the nodes in the order they are visited.
    """

    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example usage:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("BFS traversal starting from 'A':")
bfs(graph, "A")  # Output: A B C D E F
