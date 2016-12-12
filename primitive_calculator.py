#!/usr/bin/env python
import sys

### give an input, find minimum steps needed to reach to that number from 1, only by multiplication of 2 and 3 and minus 1

def optimal_sequence(n):
    sequence = {}
    count = {}
    count[1] = 0
    sequence[0]=1
    sequence[1]="1"
 
    index = 1
    
    for num in range(2,n+1):
               count[num] = 1000000
               index = index+1
           
               if num % 3 ==0:
                 count[num] = count[(num//3)] + 1
                 sequence[num] = sequence[(num//3)]
               if num % 2 ==0:
                 count_save = count[num]
                 count[num] = count[(num//2)] + 1
                 if count[num] > count_save:     ## doing this, because want to check if dividing by 2 disallow divide by 3 or increases total step
                     count[num] = count_save
                 else:
                     sequence[num] = sequence[(num//2)]
               count_save = count[num]
               count[num] = count[num-1] + 1
               if count[num] > count_save:      ## same reason as previous check
                 count[num] = count_save
               else:
                 sequence[num] = sequence[num-1]
               sequence[num]= str(sequence[num]) +" "+ str(num)

    return sequence[n].split()


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
#    print(x, end=' ')
  sys.stdout.write(x) 
  sys.stdout.write(" ")
print ""
