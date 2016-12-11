#!/usr/bin/env python

####finding majority element in given numbers
####runtime is (n * logn)

num = raw_input("Enter number of elements   ")
num = int(num)

data_string = raw_input("Enter all the numbers     ")
data = data_string.split()

for i in range(0, num):

     data[i] = int(data[i])

def majority_element(data):

#### if not at the last level...need to divide more
   if len(data) > 2:
     data_half_1 = data[: (len(data)//2)]
     data_half_2 = data[len(data)//2 :]
     feedback1 = majority_element(data_half_1)
     feedback2 = majority_element(data_half_2)      
     
   else:
       if len(data) == 1:
         return [1, data[0]]
       else:
         if data[0] == data[1]:
           return [1, data[0]]  ##first element telling whether there is a majority element, second one telling the element
         else:
           return [0, -1]   ### putting -1 assuming -1 will not be a real entry
   
   if feedback1[0] + feedback2[0] == 0 :   ## if both have no majority element
      return [0, -1]

   elif ((feedback1[0] * feedback1[0]) == 1) and (feedback1[1] == feedback2[1]) :  ##if both have same majority element
      return [1, feedback1[1]]

   elif feedback1[0] == 1 or feedback2[0] == 1: ## if either one have majority element, need to know if there is majority element after combinations
    if feedback1[0] == 1:
      total = 0
      for i in range(0, len(data_half_2)):
           if data_half_2[i] == feedback1[1]:
             total += 1
      for i in range(0, len(data_half_1)):
           if data_half_1[i] == feedback1[1]:
             total += 1
      if total > (len(data) // 2):
        return [1, feedback1[1]]

    if feedback2[0] == 1:
      total = 0
      for i in range(0,len(data_half_2) ):
           if data_half_2[i] ==feedback2[1]:
                     total += 1
      for i in range(0,len(data_half_1)):
           if data_half_1[i] ==feedback2[1]:
                     total += 1
      if total > (len(data) // 2):
           return [1, feedback2[1]]
      else:
           return [0, -1]

    return [0, -1]  

output =  majority_element(data)

print output[0] 
 
