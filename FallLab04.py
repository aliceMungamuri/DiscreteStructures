#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 04
# Description : Recursive search for X in a list of an
# Collaborators: NONE
x = int(input('What number are you searching for'))

listn = []
firstItem = 0
lastItem = len(listn)
middleSpot = (firstItem + lastItem)//2

if len(listn) == 1 and listn[0] != x: # this is if x isn't in the list
  print('0')
