# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 09
# Description : Warshalls Algorith Algorithm #2 
# Collaborators: NONE


def algorithm2(MR):
    """
    finds the transitive closure of a zero-one matrix using Warshall's algorithm (Algorithm 2).
    """
    n = len(MR)
    # Copy the input matrix to W 
    W = [row[:] for row in MR]

    # Implement Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    
    return W


def printingMatrix(matrix):
    """Utility function to print a matrix."""
    for row in matrix:
        print(' '.join(str(x) for x in row))


def getMatrixInput():
    """Function to take matrix input from the user."""
    n = int(input("Enter the size of the matrix (n): "))
    print(f"Enter the elements of the {n}x{n} matrix row by row (0 or 1) (add a space in between and a space after the last element of a row):")

    # Initialize an empty matrix
    MR = []
    
    # Taking input for each row of the matrix
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        MR.append(row)
    
    return MR


def main():
    # Get the input matrix 
    MR = getMatrixInput()


    
    # Prints the result
    print("\nTransitive Closure:")
    printingMatrix(algorithm2(MR))


main()
