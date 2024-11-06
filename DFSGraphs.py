def dfs(graph, start, visited=None):
    """
    Perform a depth-first search (DFS) on a graph starting from a given node.
    Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Keys are nodes, and values are lists of neighboring nodes.
        start: The starting node for the DFS.
        visited (set, optional): A set of nodes that have already been visited.
                                 If None, a new set will be created.
    Returns:
        None: This function prints the nodes in the order they are visited.
    """
    
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("\nDFS traversal starting from 'A':")
dfs(graph, "A")  # Output: A B D E F C
