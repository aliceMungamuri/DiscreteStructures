#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 04
# Description : Recursive search for X in a list of an
# Collaborators: NONE
x = input('What number are you searching for')
j = int(input('How many numbers in this list'))
listn = []
for i in range(j):
  add = input('What number are you adding to the list')
  listn.append(add)
def search(listn, x):
  firstItem = 0
  lastItem = len(listn)
  middleSpot = (firstItem + lastItem)//2
  if len(listn) == 1 and listn[0] != x: # this is if x isn't in the list
    print('0')
  else:
    if  listn[middleSpot] == x:
      print(middleSpot+1)
    elif  listn[middleSpot] < x:
      listn = listn[middleSpot:lastItem]
      newSearch = search(listn,x)
        # if newSearch is not False, add it to the left side of the window and return
      print(newSearch + middleSpot +1)
    elif listn[middleSpot] > x:
      listn = listn[firstItem:middleSpot]
      newSearch = search(listn,x)
      print( newSearch + firstItem +1)
search(listn,x)
    
  
