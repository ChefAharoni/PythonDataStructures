import heapq


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}  # Initialize distances
    distances[start] = 0
    priority_queue = [(0, start)]  # Min-heap based on distance

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if we've already found a better path
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

distances = dijkstra(graph, "A")
print("\nShortest distances from 'A':")
for vertex, distance in distances.items():
    print(f"Distance to {vertex}: {distance}")
