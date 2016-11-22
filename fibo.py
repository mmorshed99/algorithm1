#!/usr/bin/env python

input = raw_input("Enter the number  ")
input = int(input)

def calculate_fib(n):

   save_results = []
   save_results.append(0)
   save_results.append(1)
   if n > 1:
     for i in range(2,n+1):
    
        save_results.append( save_results[i-1] + save_results[i-2])
     return save_results[n]
   else:
     return save_results[n]

print calculate_fib(input)
