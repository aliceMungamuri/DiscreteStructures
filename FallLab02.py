#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 02
# Description : Write a program that takes input from a list of [0,7] and makes pairs from the output [A,H], from the pairs determines if its a function and if it is if it is a one-to-one, onto, or both
# Collaborators: None
input = input('Enter your input pairs in the form\n (4,F)(5,G)(4,H)\n The inputs are a list of mappings of elements from set [0,1,2,3,4,5,6,7] to the elements of set [A,B,C,D,E,F,G,H]\n 1 ≤ Number of pairs in input ≤ 16\n Do NOT put the same pair in: ex. (1,A)(B,2)(1,A)\n')
print(input)
num = 0
function = True
oneToOne = True
onto = True
checkOntoList = ['A','B','C','D','E','F','G','H']


splitInput = input.split(')(')

inputList = []
outputList = []

for i in splitInput:
  in_, out = i.split(',')
  inputList.append(in_)
  outputList.append(out)

# Checking if multiple inputs bc that means its not a function
#for i in inputList:
  #if inputList.count(i) > 1:
    #function = False

inputListSet = set()
for i in inputList:
  if i in inputListSet:
    function = False
  inputListSet.add(i)
  
  
# checking if function is onto
for i in checkOntoList:
  if i not in outputList:
    onto = False
    
# checking if function is one-to-one
 # for i in inputList:
   # if outputList.count(i) > 1:
     # oneToOne = False
outputListSet = set()
for i in outputList:
  if i in outputListSet:
    oneToOne = False
  outputListSet.add(i)
  

#printing output
if function == False:
  print('not function')
if function == True and onto == True and oneToOne == True:
  print('function, one-to-one, onto')
if function == True and onto == False and oneToOne == True:
  print('function, not onto, one-to-one')
if function == True and onto == True and oneToOne == False:
  print('function, onto, not one-to-one')
if function == True and onto == False and oneToOne == False:
  print('function, not onto, not one-to-one')
  
  
      

# Req = one to one 2 inputs cant go to one output, onto means all outputs covered not a function if an input goes to 2 outputs
  
