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

def mergeList(list1,list2):
  L = [] # new list
  if list1 == [] and list2 == []:
    return L
  if list1 != [] and list2 == []:
    L = L.append(list1)
  if list1 == [] and list2 != []:
    L = L.append(list2)
    
    
  if list1[0]<= list2[0]:
    L.append(list1[0])
    L = L + mergeList(list1[1:],list2)
  if list2[0]<= list1[0]:
    L.append(list2[0])
    L = L + mergeList(list1,list2[1:])
  setL = set(L) # for getting rid of the duplicates
  L = list(setL)
  
  return L


  
  
