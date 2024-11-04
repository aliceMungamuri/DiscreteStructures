# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 08
# Description : Output of transitive closure
# Collaborators: NONE
def transClos(actualMatrixUserInput):

    n = len(actualMatrixUserInput)
    A = [row[:] for row in actualMatrixUserInput]  
    B = [row[:] for row in actualMatrixUserInput]  

    # Initialize B as the input matrix
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]

    # Perform the algorithm: iteratively multiply and add to compute the closure
    for _ in range(n):
        A_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A_new[i][j] = int(any(A[i][k] and actualMatrixUserInput[k][j] for k in range(n)))

        # Update A for the next iteration
        A = A_new
        
        # Update B with the new connections found in A
        for i in range(n):
            for j in range(n):
                B[i][j] = int(B[i][j] or A[i][j])  # Logical OR for transitive closure

    return B

def matrixUserInput():

    n = int(input("Enter the size of the matrix (n x n): "))
    print("Enter the matrix values row by row, separated by spaces (Enter a space after the last element of a row):")
    actualMatrixUserInput = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        actualMatrixUserInput.append(row)
    return actualMatrixUserInput

def main ():
    # Get user input for the matrix
    actualMatrixUserInput = matrixUserInput()

    # Compute the transitive closure
    actualMatrixUserInput_closure = transClos(actualMatrixUserInput)

    # Print the result without brackets and with space-separated values
    print("Transitive Closure:")
    for row in actualMatrixUserInput_closure:
        print(" ".join(str(x) for x in row))
main()
