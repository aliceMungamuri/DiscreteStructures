# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 06
# Description : Output of Bit Sequences
# Collaborators: NONE

def makeSequence(n, current_sequence="", lastNum="", newString=""):
    if len(current_sequence) == n:
        newString += current_sequence + ", "
        return newString  #returns the new string
    
    # new sequences by adding 1 and 0
    if lastNum != "0":
        newString = makeSequence(n, current_sequence + "0", "0", newString)
        newString = makeSequence(n, current_sequence + "1", "1", newString)
    
    return newString

def main():
    n = int(input("Enter an integer (1 <= n <= 32): "))
    
    if n == 1:
        print("Output for n=1: 0, 1")
        return
    
    print(f"Output for integer={n}: ", end="")
    newString = makeSequence(n)
    print(newString[:-2])  # Slice off the last comma and space bc I couldn't figure out how to do it inside the recursive function

main()
