#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 04
# Description : Recursive search for X in a list of an
# Collaborators: NONE
x = int(input('What number are you searching for'))

listn = []
def search(listn, x):
  firstItem = 0
  lastItem = len(listn)
  middleSpot = (firstItem + lastItem)//2
  if len(listn) == 1 and listn[0] != x: # this is if x isn't in the list
    print('0')
  if  listn[middleSpot] == x:
    return middleSpot
  elif  listn[middleSpot] < x:
    listn = listn[middleSpot:lastItem]
    newSearch = search(listn,x)
        # if v is not False, add it to the left side of the window and return
        # else return False
        return newSearch + middleSpot if newSearch != False else newSearch
    elif listn[middleSpot] > x:
        listn = listn[firstItem:middleSpot]
        newSearch = search(listn,x)
        return newSearch + firstItem if newSearch != False else newSearch
