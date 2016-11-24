#!/usr/bin/env python

###### The first line of input contains number n of items and capacity W of knapsack.The next n lines define the values and
###### weights of the items. The i-th line contains integers v and w, the value and weight of i-th item. Given amounts are maximum
###### possible amounts

items_and_cap = raw_input("Enter number of items and capacity with space  ")

items_and_cap_split = items_and_cap.split()

number_of_items = int(items_and_cap_split[0])

capacity = int(items_and_cap_split[1])

lines = []

value = []

weight = []

value_per_weight = []

for i in range(0, number_of_items):

     lines.append(raw_input())
     temp = lines[i].split()
     value.append (int(temp[0]))
     weight.append(int(temp[1]))
     value_per_weight.append(value[i] / float(weight[i]))

amount_value = 0
amount_weight = 0

### Sorting here based on value per weight###

for i in range(0,number_of_items):
   
   for j in range(i+1,number_of_items):
 
      if value_per_weight[j] > value_per_weight[i]:
        temp_value_per_weight = value_per_weight[i]
        temp_value = value[i]
        temp_weight = weight[i]

        value_per_weight[i] = value_per_weight[j]
        value[i] = value[j]
        weight[i] = weight[j]

        value_per_weight[j] = temp_value_per_weight
        value[j] = temp_value
        weight[j] = temp_weight


if  capacity > 0:

     for i in range(0, number_of_items):

        if amount_weight + weight[i] < capacity:
          amount_weight += weight[i]
          amount_value += value[i]
        else:
          added_weight = capacity - amount_weight
          amount_value += added_weight * value_per_weight[i]
          break 
         

print amount_value
