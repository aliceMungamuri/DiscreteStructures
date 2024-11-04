# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 08
# Description : Output of transitive closure
# Collaborators: NONE
import numpy as np

def transitive_closure(M_R):
    # Initialize A and B as given in the algorithm
    A = M_R.copy()
    B = A.copy()
    n = len(M_R)
    
    # Perform the algorithm
    for i in range(2, n + 1):
        A = np.dot(A, M_R)  # Boolean matrix multiplication (using dot product here)
        A = np.clip(A, 0, 1)  # Ensure entries remain 0 or 1
        B = np.bitwise_or(B, A)  # Boolean matrix addition (using bitwise OR)
    
    return B

# Example usage
M_R = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
])

M_R_closure = transitive_closure(M_R)
print("Transitive Closure:")
print(M_R_closure)
