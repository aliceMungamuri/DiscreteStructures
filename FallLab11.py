# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 11
# Description:dMethods method
# Collaborators: NONE
import math
def dMethod(graph, start, end):
    """
    Find the shortest path between two vertices =using Algorithm 1 from 10.6 - for this use alt 236 to use infinity

    """

    # makes the distances and previous nodes
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    pastNode = {vertex: None for vertex in graph}
    unvisited = set(graph.keys())

    while unvisited:
        #   this chooses the shortest
        curVertex = min(unvisited, key=lambda vertex: distances[vertex])

        #  shows thst when it stops
        if curVertex == end:
            break

        unvisited.remove(curVertex)

        for neighbor, weight in graph[curVertex].items():
            if neighbor in unvisited:
                replaceDistance = distances[curVertex] + weight
                if replaceDistance < distances[neighbor]:
                    distances[neighbor] = replaceDistance
                    pastNode[neighbor] = curVertex

    # Reconstruct the shortest path
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = pastNode[current]

    return path, distances[end]


def LookInput():
    # the first row is the the letters like the row names (a b c d)
    """
    look through  the graph and vertices.

    returns a tuple
    """

    print("Enter the matrix (use ∞ (that is alt and 236 on the number pad) for infinity):")
    vertices = input().split()  
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
    graph, start, end = LookInput()
    path, distance = dMethod(graph, start, end)
    print("Shortest path:", ", ".join(path))
    print("Path length:", distance)


main()
