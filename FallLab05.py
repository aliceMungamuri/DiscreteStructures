# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
# LAB Assignment 05
# Description: Merge two ordered lists of positive integers
# Collaborators: NONE

list1 = []  # the lists
list2 = []

# for setting the lists up
n = int(input('Enter the number of elements for list 1: '))
for i in range(0, n):
    element = int(input('Put your element (remember in increasing order and 1 ≤ n ≤ 32, 1 ≤ m ≤ 32): '))
    list1.append(element)

n = int(input('Enter the number of elements for list 2: '))
for i in range(0, n):
    element = int(input('Put your element (remember in increasing order and 1 ≤ n ≤ 32, 1 ≤ m ≤ 32): '))
    list2.append(element)

def mergeList(list1, list2):
    # Base cases for recursion
    if not list1:  # If list1 is empty
        return list2  # Return list2
    if not list2:  # If list2 is empty
        return list1  # Return list1

    # Recursive merging logic
    if list1[0] < list2[0]:
        # Include the first element of list1 and recurse
        return [list1[0]] + mergeList(list1[1:], list2) if list1[0] not in list2 else mergeList(list1[1:], list2)
    elif list1[0] > list2[0]:
        # Include the first element of list2 and recurse
        return [list2[0]] + mergeList(list1, list2[1:]) if list2[0] not in list1 else mergeList(list1, list2[1:])
    else:
        # Both elements are equal; skip one and recurse
        return mergeList(list1[1:], list2[1:])

# Print the merged list
result = mergeList(list1, list2)
# Removing duplicates from the final output
result = list(dict.fromkeys(result))  # Maintain order while removing duplicates
print(result)
