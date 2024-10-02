list1 = [] # the lists
list2 = []

lengthList1 = len(list1) # i dont think these are necessary
lengthList2 = len(list2)
i = 0
j = 0

def mergeList(list1,list2):
  L = [] # new list
  if list1[0]<= list2[0]:
    L.append([list1])
  
