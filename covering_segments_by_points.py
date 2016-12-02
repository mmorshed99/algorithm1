#!/usr/bin/env python

#### You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that
#### each segment contains at least one marked point.
#### Given a set of n segments (a0, b0),(a1, b1) with integer coordinates on a line, find
#### the minimum number m of points such that each segment contains at least one point.

number_of_segments = raw_input("Enter number of integer  ")
number_of_segments = int(number_of_segments)

points = []
segment_length = []
points_coordinates = []

for i in range(0,number_of_segments):

     points.append(raw_input())
     points_split = points[i].split()
     points_split[0] = int(points_split[0])
     points_split[1] = int(points_split[1])
     diff = abs(points_split[0] - points_split[1])
     segment_length.append(diff)
     points_coordinates.append([])
     points_coordinates[i].append(points_split[0])
     points_coordinates[i].append(points_split[1])
     
#### sorting the segments based on their lengths ####

for i in range(0,number_of_segments):

     for j in range(i,number_of_segments):

          if segment_length[j] < segment_length[i]:

            segment_length[i], segment_length[j] = segment_length[j], segment_length[i]
            points_coordinates[i][0], points_coordinates[j][0] = points_coordinates[j][0], points_coordinates[i][0]
            points_coordinates[i][1], points_coordinates[j][1] = points_coordinates[j][1], points_coordinates[i][1] 
             

points_count = 0
points_loc = []


while len(segment_length) > 0:

     highest_points_covered_index = points_coordinates[0][0]
     highest_points_covered_sofar = 1
     for i in range(points_coordinates[0][0], points_coordinates[0][1] + 1):
       current_highest_points = 1
       if len(segment_length) > 1:
          for j in range(1, len(segment_length)  ):

               if (i >= points_coordinates[j][0]) and (i <= points_coordinates[j][1]) :
                      current_highest_points += 1

          if current_highest_points >= highest_points_covered_sofar:

            highest_points_covered_sofar = current_highest_points
            highest_points_covered_index = i

     points_loc.append(highest_points_covered_index)
     points_count += 1
     
#### Now let's delete the segments already covered with this point ####
     need_to_del = []
     if len(segment_length) > 1:
       for j in range(1, len(segment_length)):
          if (highest_points_covered_index  >= points_coordinates[j][0]) and (highest_points_covered_index <= points_coordinates[j][1]):
            need_to_del.append(j)
       need_to_del.reverse()
       for k in need_to_del:
          del segment_length[k]
          del points_coordinates[k]
     del segment_length[0]
     del points_coordinates[0]  
print points_count
#print ','.join(points_loc)
print str(points_loc)[1:-1] ## removing brackets and using this as they are integers

