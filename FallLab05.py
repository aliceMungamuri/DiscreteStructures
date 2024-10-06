#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 05
# Description : Merge Sort of a list
# Collaborators: NONE
list1 = [] # the lists
list2 = []

lengthList1 = len(list1) # i dont think these are necessary
lengthList2 = len(list2)
i = 0
j = 0

# for setting the lists up
n = int(input('Enter the number of elements for list 1: '))
for i in range(0,n):
  element = int(input('Put your element (remember in increasing order and 1 ≤ n ≤ 32, 1 ≤ m ≤ 32 )'))
  list1.append(element)
n = int(input('Enter the number of elements for list 2: '))
for i in range(0,n):
  element = int(input('Put your element (remember in increasing order and 1 ≤ n ≤ 32, 1 ≤ m ≤ 32 )'))
  list2.append(element)

def mergeList(list1, list2):
    L = []  # new list
    
    # Base cases for recursion
    if not list1:  # If list1 is empty
        return list2  # Return list2
    if not list2:  # If list2 is empty
        return list1  # Return list1

    # Recursive merging logic
    if list1[0] < list2[0]:  # If the first element of list1 is smaller
        L.append(list1[0])  # Add the first element of list1
        L += mergeList(list1[1:], list2)  # Recur with the rest of list1
    elif list1[0] > list2[0]:  # If the first element of list2 is smaller
        L.append(list2[0])  # Add the first element of list2
        L += mergeList(list1, list2[1:])  # Recur with the rest of list2
    else:  # They are equal
        L.append(list1[0])  # Add one of the equal elements (from either list)
        L += mergeList(list1[1:], list2[1:])  # Recur with the rest of both lists

    return L
print(mergeList(list1,list2))


  
  
