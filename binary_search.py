#!/usr/bin/env python


### Implementing binary search. 1st line inputs number of elements and all elements from low to high
### 2nd line gives number of elements and all elements to search for. Outputs -1 if not present or index 
### othersise


items = raw_input("Enter the number of items and numbers in order  ")
items_splitted = items.split()
for i in range(0,len(items_splitted)):
     items_splitted[i] = int(items_splitted[i])

search = raw_input("Enter the number of items and numbers to look for  ")
search_numbers = search.split()
for i in range(0,len(search_numbers)):
     search_numbers[i] = int(search_numbers[i])

def binary_search(storage, search):

   total_numbers = storage.pop(0)
   
   total_to_search = search.pop(0)

   indexes = []
   for i in range(0, total_to_search):

         left = 0
         right = total_numbers-1
        
         while(True):

              mid = left + (right - left) // 2


              if search[i] == storage[mid]:
                  indexes.append(mid)
                  break

              
              elif mid == left:
                if search[i] == storage[right]:
                  indexes.append(right)
                  break
                indexes.append(-1)
                break

              elif search[i] == storage[mid]:  
                  indexes.append(mid)
                  break 

              elif search[i] > storage[mid]:
                  left = mid
                  continue

              elif search[i] < storage[mid]:
                  right = mid
                  continue
   return str(indexes)[1:-1]
print binary_search(items_splitted, search_numbers)              
 
