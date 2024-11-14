ementation
python
Copy code
def find_euler_circuit(adj_matrix):
    n = len(adj_matrix)  # Size of the graph
    # Create a graph using adjacency matrix
    graph = {chr(97 + i): [] for i in range(n)}  # Mapping from 0,1,2,... to 'a','b','c',...
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                graph[chr(97 + i)].append(chr(97 + j))
                graph[chr(97 + j)].append(chr(97 + i))
    
    # Function to find Euler Circuit using Hierholzer's algorithm
    def euler_circuit(start_vertex):
        circuit = []
        stack = [start_vertex]
        while stack:
            v = stack[-1]
            if graph[v]:
                # There are unused edges, take the next one
                next_vertex = graph[v].pop()
                graph[next_vertex].remove(v)  # Remove the reverse edge
                stack.append(next_vertex)
            else:
                # No unused edges, add vertex to circuit and backtrack
                circuit.append(stack.pop())
        return circuit
    
    # Start from any vertex, here we start with 'a'
    start = 'a'
    return euler_circuit(start)

# Input
adj_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Generate the Euler circuit
circuit = find_euler_circuit(adj_matrix)

# Output
print(', '.join(circuit))
