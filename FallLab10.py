# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 10
# Description: Constructing Euler's Circuit with User Input
# Collaborators: NONE


# find the euler circuit
def eulerCircuit(matrix, vertices):
    n = len(matrix)
    
    # Create a graph 
    graph = {vertices[i]: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                graph[vertices[i]].append(vertices[j])
                graph[vertices[j]].append(vertices[i])
    
    #  finds a subcircuit from thee vertex that is given 
    def getSub(start_vertex):
        subcircuit = []
        stack = [start_vertex]
        while stack:
            v = stack[-1]
            if graph[v]:
#removes the edges
                nextVert = graph[v].pop()
                graph[nextVert].remove(v)
                stack.append(nextVert)
            else:
                subcircuit.append(stack.pop())
        return subcircuit

    #  Find an initial circui from the frist vertex
    start_vertex = vertices[0]
    circuit = getSub(start_vertex)
    
    # remove the edges from the graph
    H = {v: edges[:] for v, edges in graph.items()}

    # adding subcircuits
    i = 0
    while i < len(circuit):
        vertex = circuit[i]
        if H[vertex]:
            subcircuit = getSub(vertex)
            
            # inserts subcircuit in pos i
            circuit = circuit[:i] + subcircuit + circuit[i+1:]
        i += 1

    return circuit

# takes the user input - tbh I really was consude how to set this up
def getMatrix():
# this takes the vertices first
    vertices = input("Enter the vertices ( remember space-separated): ").split()
    n = len(vertices)
    
#putting in the actual adj matrix with the row labels (like a b c d)
    matrix = []
    print("Enter the adjacency matrix with row labels:")
    for i in range(n):
        row_input = input().split()
        row = list(map(int, row_input[1:]))  # so it doesnt take the letter
        matrix.append(row)
    
    return matrix, vertices

# Main execution
matrix, vertices = getMatrix()
circuit = eulerCircuit(matrix, vertices)

# Output the result
print( ', '.join(circuit))
