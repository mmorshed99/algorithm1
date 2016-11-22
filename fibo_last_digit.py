#!/usr/bin/env python     

input = raw_input("Enter the Number   ")

input = int(input)

def fibo_last_digit(n):

   saved_fib = []
   for i in range(0,n+1):
      if i <=1:
        saved_fib.append(i)

      else:
        saved_fib.append((saved_fib[i-1] % 10) + (saved_fib[i-2] % 10))

   return saved_fib[n] % 10

print fibo_last_digit(input)  
