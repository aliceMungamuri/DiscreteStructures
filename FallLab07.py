# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 06
# Description : Output of Bit Sequences
# Collaborators: NONE

def makeSequence(n, current_sequence="", lastNum="", output=""):
    if len(current_sequence) == n:
        output += current_sequence + ", "
        return output  # Return the updated output string
    
    # Generate sequences by adding "1" and, if applicable, "0"
    if lastNum != "0":
        output = makeSequence(n, current_sequence + "0", "0", output)
    output = makeSequence(n, current_sequence + "1", "1", output)
    
    return output

def main():
    n = int(input("Enter an integer (1 <= n <= 32): "))
    
    if n == 1:
        print("Output for n=1: 0, 1")
        return
    
    print(f"Output for integer={n}: ", end="")
    output = makeSequence(n)
    print(output[:-2])  # Slice off the last comma and space

main()
