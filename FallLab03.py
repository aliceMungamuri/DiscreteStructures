str#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 03
# Description : Write a program that implements the algorithm for fast modular exponentiation 
# Collaborators: None
# Goal of lab: exponentiation by squaring
 # 
b = int(input ('What is your base\n1 ≤ b ≤ 100\n'))
n = int(input ('What is your exponent\n 1 ≤ n ≤ 500\n'))
m = int(input ('What is your modulus\n1 ≤ m ≤ 500.\n'))
ogN = n
res = 0
# base of just b mod m
base = b%m
# need to keep on going until exponent is o 

 while n>0:
  if n%2 ==1: # checks that if its odd updates result, in binary exponentiation,  odd exponent means need to include the current base in the result least sig bit is 1.
   res = (res*base)%m
  n = n//2 # move to next high bit --> makes it smaller
  base = (base*base)%m # taking mmod m of the square
print(f"{str(b)}^{str(ogN)} mod {str(m)} = {str(res)}")
  

    
   



    
