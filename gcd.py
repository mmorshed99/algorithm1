#!/usr/bin/env python

input1 = raw_input("Enter the number1  ")
input1 = int(input1)

input2 = raw_input("Enter the number2  ")
input2 = int(input2)

def find_gcd(a,b):

   minimum_number = min(a,b)
   if minimum_number == 1:
     return 1

   remainder = max(a,b) % minimum_number

   if remainder == 0:
     return minimum_number

   else:

     return find_gcd(remainder, minimum_number)


print find_gcd(input1,input2)
