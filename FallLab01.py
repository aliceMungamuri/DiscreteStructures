#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 01
# Description : Write a program that takes 2 inputs strings and produces them as output of bitwise and, or or XOR
# Collaborators: NONE
string1 = input('Enter your 2 bit strings with a length greater than or equal to 1 and less than or equal to 32')
string2 = input('Enter your 2 bit strings with a length greater than or equal to 1 and less than or equal to 32')
n = len(string1)
bitAnd = ''
bitOr = ''
bitXor = ''
resultAnd = []
resultOr = []
resultXor = []
for i in range (n):
  if string1[i] == 1 and  string2[i] == 1:
    bitAnd = '1'
    resultAnd.append(bitAnd)
  else:
    bitAnd = '0'
    resultAnd.append(bitAnd)
  if string1[i] == 1 or  string2[i] == 1:
    bitOr = '1'
    resultAnd.append(bitOr)
  else:
    bitOr = '0'
    resultAnd.append(bitOr)
  if string1[i] != string2[i] :
    bitXor = '1'
    resultAnd.append(bitXor)
  else:
    bitXor = '0'
    resultAnd.append(bitXor)


print(f'Bitwise And result is {resultAnd} Bitwise Or result is {resultOr} Bitwise XOR result is {resultXor}')
