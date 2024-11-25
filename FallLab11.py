def dijkstra(graph, start, end):
    """
    Find the shortest path between two vertices using Dijkstra's algorithm.

    Parameters:
    graph (dict): Weighted adjacency list representation of the graph.
    start (str): Starting vertex.
    end (str): Destination vertex.

    Returns:
    tuple: (shortest path as a list of vertices, total weight of the path).
    """
    import math

    # Initialize distances and previous nodes
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
    unvisited = set(graph.keys())

    while unvisited:
        # Select the vertex with the smallest distance
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # If we've reached the destination, stop
        if current_vertex == end:
            break

        unvisited.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if neighbor in unvisited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_vertex

    # Reconstruct the shortest path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[end]


def parse_input():
    """
    Parse the input for the graph and vertices.

    Returns:
    tuple: (graph as an adjacency list, start vertex, end vertex)
    """
    import math

    print("Enter the weighted adjacency matrix (use ∞ for infinity):")
    vertices = input().split()  # First row contains the vertex names
    graph = {vertex: {} for vertex in vertices}

    for i, row in enumerate(vertices):
        weights = input().split()
        for j, weight in enumerate(weights):
            if weight != "∞":
                graph[row][vertices[j]] = int(weight)

    print("Enter the start and end vertices (separated by space):")
    start, end = input().split()
    return graph, start, end


def main():
    graph, start, end = parse_input()
    path, distance = dijkstra(graph, start, end)
    print("Shortest path:", ", ".join(path))
    print("Path length:", distance)


if __name__ == "__main__":
    main()
