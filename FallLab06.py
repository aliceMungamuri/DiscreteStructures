#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 06
# Description : Next Permutation
# Collaborators: NONE

def getNextPerm(num):
  # make the input number into a list
  
  digits = [int(d) for d in str(num)]
  j = len(digits) - 2  # need the largest j so jk < j(k+1)

  while j >= 0 and digits[j] >= digits[j + 1]:
    j -= 1
  if j < 0:
    return "No next permutation"

    # k>j smallest index for that point
  k = len(digits) - 1
  while digits[k] <= digits[j]:
    k -= 1

    # switch the cells of dig[k] with dig[j]
  digits[j], digits[k] = digits[k], digits[j]

    # j+1 to the end
  digits = digits[:j + 1] + digits[j + 1:][::-1]

    #.join makes it back into a number
  return int("".join(map(str, digits)))



output = int(input('What is your number with n digits (no repetition) 1<= n <=10: '))
print(getNextPerm(output))
