# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 09
# Description : Warshalls Algorith Algorithm #2 
# Collaborators: NONE


def warshall_algorithm(M_R):
    """
    Compute the transitive closure of a zero-one matrix using Warshall's algorithm.
    
    Parameters:
    M_R (list of lists): A square matrix (n x n) with binary entries (0 or 1).
    
    Returns:
    list of lists: The transitive closure of the matrix M_R.
    """
    n = len(M_R)
    # Copy the input matrix to W (no need for numpy)
    W = [row[:] for row in M_R]

    # Implement Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    
    return W


def print_matrix(matrix):
    """Utility function to print a matrix."""
    for row in matrix:
        print(' '.join(str(x) for x in row))


def get_user_input():
    """Function to take matrix input from the user."""
    n = int(input("Enter the size of the matrix (n): "))
    print(f"Enter the elements of the {n}x{n} matrix row by row (0 or 1):")

    # Initialize an empty matrix
    M_R = []
    
    # Taking input for each row of the matrix
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        # Ensure the row has exactly n elements
        if len(row) != n:
            print(f"Error: Each row must have exactly {n} elements.")
            return None
        M_R.append(row)
    
    return M_R


def main():
    # Get the input matrix from the user
    M_R = get_user_input()
    
    # If the matrix input is invalid, exit the program
    if M_R is None:
        return

    # Compute transitive closure
    transitive_closure = warshall_algorithm(M_R)
    
    # Print the result
    print("\nTransitive Closure:")
    print_matrix(transitive_closure)


if __name__ == "__main__":
    main()
