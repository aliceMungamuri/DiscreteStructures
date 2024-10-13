#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 06
# Description : Next Permutation
# Collaborators: NONE

def next_permutation(num):
  # Convert the input number to a list of digits
  digits = [int(d) for d in str(num)]
  j = len(digits) - 2  # Step 1: Find the largest index j such that digits[j] < digits[j + 1]

  while j >= 0 and digits[j] >= digits[j + 1]:
    j -= 1
  if j < 0:
    return "No next permutation"

    # Step 2: Find the smallest index k greater than j such that digits[k] > digits[j]
  k = len(digits) - 1
  while digits[k] <= digits[j]:
    k -= 1

    # Step 3: Swap digits[j] with digits[k]
  digits[j], digits[k] = digits[k], digits[j]

    # Step 4: Reverse the sequence from j + 1 to the end of the list
  digits = digits[:j + 1] + digits[j + 1:][::-1]

    # Convert the list of digits back to a number
  return int("".join(map(str, digits)))



output = input(int('What is your number with n digits (no repetition) 1<= n <=10: '))
print(next_permutation(output))
