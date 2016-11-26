#!/usr/bin/env python

###### Given two sequences a1,a2...an and b1,b2....bn, find a permutation of second sequence such that dot product of two sequences is minimum   #####
###### The first line contains number of elements in each sequence, second line contains first sequence and third line contains second sequence  #####

number_of_elems = raw_input("Enter number of elements   ")
number_of_elems = int(number_of_elems)

first_seq = raw_input("Enter the first sequence   ")
second_seq = raw_input("Enter the second sequence  ")

first_seq_split = first_seq.split()
second_seq_split = second_seq.split()

for i in range(0, number_of_elems):
   first_seq_split[i] = int(first_seq_split[i])
   second_seq_split[i] = int(second_seq_split[i])


##### Let's sort both the sequences #####

for i in range(0, number_of_elems):

     for j in range(i, number_of_elems):

        if first_seq_split[j] > first_seq_split[i]:

          temp = first_seq_split[i]
          first_seq_split[i] = first_seq_split[j]
          first_seq_split[j] = temp

        if second_seq_split[j] < second_seq_split[i]:

          temp = second_seq_split[i]
          second_seq_split[i] = second_seq_split[j]
          second_seq_split[j] = temp

sum = 0

for i in range(0, number_of_elems):

     sum += first_seq_split[i] * second_seq_split[i]


print sum
