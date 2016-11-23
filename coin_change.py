#!/usr/bin/env python

####### Find the minimum number of coins to change the input value(an integer) into coins with denominations 1, 5 and 10 #####

input = raw_input("Enter the money amount   ")

input = int(input)

def find_change(a):

   count = 0

   while a > 0:

        if a >= 10:
          count += (a//10)
          a = a - (a//10) * 10

        if a>= 5:
          count += (a//5)
          a = a - (a//5) * 5

        if a>= 1:
          count += a 
          a = a - a

   return count


print find_change(input)
