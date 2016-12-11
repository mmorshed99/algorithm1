#!/usr/bin/env python

####finding majority element in given numbers


num = raw_input("Enter number of elements   ")
num = int(num)

data_string = raw_input("Enter all the numbers     ")
data = data_string.split()

for i in range(0, num):

     data[i] = int(data[i])

def majority_element(data):


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
           return [1, data[0]]
         else:
           return [0, -1]
   
   if feedback1[0] + feedback2[0] == 0 :
      return [0, -1]

   elif ((feedback1[0] * feedback1[0]) == 1) and (feedback1[1] == feedback2[1]) :
      return [1, feedback1[1]]

   elif feedback1[0] == 1 or feedback2[0] == 1:
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
 
