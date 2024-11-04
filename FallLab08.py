# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 08
# Description : Output of transitive closure
# Collaborators: NONE
def transitive_closure(M_R):
    """
    Compute the transitive closure of a zero-one matrix M_R using matrix multiplication and boolean addition.

    Parameters:
    M_R (list of list of int): A square matrix of size n x n with binary entries (0 or 1).

    Returns:
    list of list of int: The transitive closure of the matrix M_R.
    """
    if not M_R or len(M_R) != len(M_R[0]):
        raise ValueError("Input must be a non-empty square matrix.")

    n = len(M_R)
    A = [row[:] for row in M_R]  # Deep copy of M_R
    B = [row[:] for row in M_R]  # Initialize B as a copy of A

    for _ in range(2, n + 1):
        A_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A_new[i][j] = int(any(A[i][k] and M_R[k][j] for k in range(n)))
        
        A = A_new
        
        for i in range(n):
            for j in range(n):
                B[i][j] = int(B[i][j] or A[i][j])  # Convert boolean to int

    return B

if __name__ == "__main__":
    # Example input
    M_R = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 0]
    ]

    # Compute the transitive closure
    M_R_closure = transitive_closure(M_R)

    # Print the result without brackets and with space-separated values
    print("Transitive Closure:")
    for row in M_R_closure:
        print(" ".join(str(x) for x in row))
