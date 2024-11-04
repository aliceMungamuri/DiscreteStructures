# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 08
# Description : Output of transitive closure
# Collaborators: NONE
def transitive_closure(M_R):

    n = len(M_R)
    A = [row[:] for row in M_R]  
    B = [row[:] for row in M_R]  #   as a copy of 

    # Initialize B as the input matrix M_R
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]

    # Perform the algorithm: iteratively multiply and add to compute the closure
    for _ in range(n):
        A_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A_new[i][j] = int(any(A[i][k] and M_R[k][j] for k in range(n)))

        # Update A for the next iteration
        A = A_new
        
        # Update B with the new connections found in A
        for i in range(n):
            for j in range(n):
                B[i][j] = int(B[i][j] or A[i][j])  # Logical OR for transitive closure

    return B

def get_matrix_input():

    n = int(input("Enter the size of the matrix (n x n): "))
    print("Enter the matrix values row by row, separated by spaces (Enter a space after the last element of a row):")
    M_R = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        M_R.append(row)
    return M_R

def main ():
    # Get user input for the matrix
    M_R = get_matrix_input()

    # Compute the transitive closure
    M_R_closure = transitive_closure(M_R)

    # Print the result without brackets and with space-separated values
    print("Transitive Closure:")
    for row in M_R_closure:
        print(" ".join(str(x) for x in row))
main()
