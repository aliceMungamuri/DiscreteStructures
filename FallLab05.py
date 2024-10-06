# Name: Alice Mungamuri
# KUID: 3117704
# Lab Session: Monday 8am
# Lab Assignment 05
# Description: Recursive Binary Search to find the position of an integer in an ordered list

# Function to perform recursive binary search
def recursive_binary_search(lst, target, low, high):
    # Base case: target is not found
    if low > high:
        return 0
    
    # Find the middle index
    mid = (low + high) // 2
    
    # Check if the middle element is the target
    if lst[mid] == target:
        return mid + 1  # Convert to 1-based index
    
    # If target is smaller, search the left half
    elif target < lst[mid]:
        return recursive_binary_search(lst, target, low, mid - 1)
    
    # If target is larger, search the right half
    else:
        return recursive_binary_search(lst, target, mid + 1, high)

# Input section
n = int(input('Enter the number of elements for the list: '))
lst = []

# Collect elements of the list
for i in range(n):
    element = int(input(f'Enter element {i+1} (in increasing order): '))
    lst.append(element)

# Input the target integer
target = int(input('Enter the target integer to search for: '))

# Call the binary search function
position = recursive_binary_search(lst, target, 0, n - 1)

print(position)
