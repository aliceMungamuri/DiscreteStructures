# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session: Monday 8am
# Lab Assignment 05
# Description: Recursive Binary Search to find the position of an integer in an ordered list

def recursive_binary_search(lst, target, low, high):
    # Base case basically when the target isnt in the list
    if low > high:
        return 0
    
    # Find the middle place
    mid = (low + high) // 2
    
    # is mid in the target
    if lst[mid] == target:
        return mid + 1  # bc index starts at 0
    
    # If targets smaller
    elif target < lst[mid]:
        return recursive_binary_search(lst, target, low, mid - 1)
    
    # If target is larger
    else:
        return recursive_binary_search(lst, target, mid + 1, high)

n = int(input('Enter the number of elements for the list: '))
lst = []

# the elements for the list
for i in range(n):
    element = int(input(f'Enter element {i+1} (in increasing order): '))
    lst.append(element)

# Input the target num
target = int(input('Enter the target number your looking for in the list: '))
#calling the function
position = recursive_binary_search(lst, target, 0, n - 1)

print(position)
