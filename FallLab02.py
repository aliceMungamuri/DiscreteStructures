#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 02
# Description : Write a program that takes input from a list of [0,7] and makes pairs from the output [A,H], from the pairs determines if its a function and if it is if it is a one-to-one, onto, or both
# Collaborators: None

input = input('Enter your input pairs in the form\n (4,F)(5,G)(4,H)\n The inputs are a list of mappings of elements from set [0,1,2,3,4,5,6,7] to the elements of set [A,B,C,D,E,F,G,H]\n 1 ≤ Number of pairs in input ≤ 16\n')
print(input)

splitInput = input.split(')(')

inputList = []
outputList = []

for i in splitInput:
  in, out = i.split(',')
  inputList.append(in)
  outputList.append(out)
print(inputList)
print(outputList)
