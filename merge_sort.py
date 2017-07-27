#!/usr/bin/env python
def merge_sort(A):
   new_A = []
   if len(A) == 1:
     return A
   elif len(A) == 2:
     if A[0] > A[1]:
       new_A.append(A[1])
       new_A.append(A[0])
     else:
       new_A = A
     return new_A
   else:     
     A_left = merge_sort(A[0:(len(A)//2)])
     A_right = merge_sort(A[len(A)//2:len(A)])
     curr_index_left = 0
     curr_index_right = 0
     while(True):
           if A_left[curr_index_left] < A_right[curr_index_right] :
             new_A.append(A_left[curr_index_left])
             curr_index_left += 1
           else:
             new_A.append(A_right[curr_index_right])
             curr_index_right += 1
           if curr_index_left == len(A_left) and curr_index_right == len(A_right):
             break
           if curr_index_left == len(A_left):
             for i in range(curr_index_right,len(A_right)):
               new_A.append(A_right[i])
             break
           if curr_index_right == len(A_right):
             for i in range(curr_index_left,len(A_left)):
               new_A.append(A_left[i])
             break
     return new_A 
A = [5,1,6,9,10,4,2,1,-4]
print(A)
print(merge_sort(A))
             
