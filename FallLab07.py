#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 06
# Description : Next Permutation
# Collaborators: NONE

def generate_sequences(lengthSequences, current_sequence="", lastNum=""):
    if len(current_sequence) == lengthSequences:
        print(current_sequence, end=", ")
        return
    
    # Add 1 to the current sequence
    generate_sequences(lengthSequences, current_sequence + "1", "1")
    
    # Add 0 to the current sequence only if the last digit is not 0
    if lastNum != "0":
        generate_sequences(lengthSequences, current_sequence + "0", "0")

def main():
    lengthSequences = int(input("Enter an integer (1 ≤ n ≤ 32): "))
  # Handle base case for n = 1
    if n == 1:
        print("Output for n=1: 0, 1, ", end="")
        return
    print(f"Output for integer={lengthSequences}: ", end="")
    generate_sequences(n)

main()
