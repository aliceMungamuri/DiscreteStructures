#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 01
# Description : Write a program that takes 2 inputs strings and produces them as output of bitwise and, or or XOR
# Collaborators: NONE
string1 = input('Enter your 2 bit strings with a length greater than or equal to 1 and less than or equal to 32: ')
string2 = input('Enter your 2 bit strings with a length greater than or equal to 1 and less than or equal to 32: ')
n = len(string1)
resultAnd = []
resultOr = []
resultXor = []
for i in range (n):
  if string1[i] == '1' and  string2[i] == '1':
    resultAnd.append('1')
  else:
    resultAnd.append('0')
for i in range (n):
  if string1[i] == '1' or  string2[i] == '1':
    resultOr.append('1')
  else:
    resultOr.append('0')
for i in range (n):
  if string1[i] != string2[i] :
    resultXor.append('1')
  else:
    resultXor.append('0')


print(f'Bitwise And result is {resultAnd} Bitwise Or result is {resultOr} Bitwise XOR result is {resultXor}')
