#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 06
# Description : Next Permutation
# Collaborators: NONE

def getNextPerm(num):
  # make the input number into a list
  indNum = [int(d) for d in str(num)]
  j = len(indNum) - 2  # need the largest j so jk < j(k+1)

  while j >= 0 and indNum[j] >= indNum[j + 1]:
    j -= 1
  if j < 0:
    return "No next permutation"

    # k>j smallest index for that point
  k = len(indNum) - 1
  while indNum[k] <= indNum[j]:
    k -= 1

    # switch the cells of indNum[k] with indNum[j]
  indNum[j], indNum[k] = indNum[k], indNum[j]

    # j+1 to the end
  indNum = indNum[:j + 1] + indNum[j + 1:][::-1]

    #.join makes it back into a number
  return int("".join(map(str, indNum)))



output = int(input('What is your number with n digits (no repetition) 1<= n <=10: '))
print(getNextPerm(output))
