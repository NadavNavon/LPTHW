#!/usr/bin/env python

import csv
import numpy as np

with open("Azimuth_last.txt", "rb") as f:
   rows = csv.reader(f, delimiter='\t')


   Id = []
   Xs = []
   Xe = []
   Ys = []
   Ye = []
   Le = []
   Az = []

   for i in rows:
    if i[0] != 'Id'  and i[1] != 'Xs' and i[2] != 'Xe' and i[3] != 'Ys' and i[4] != 'Ye' and i[5] != 'Lengh' and i[6] != 'Azimuth': 
      #if is_float_covertable(i[])
        Id.append(float(i[0]))
        Xs.append(float(i[1]))
        Xe.append(float(i[2]))
        Ys.append(float(i[3]))
        Ye.append(float(i[4]))
        Le.append(float(i[5]))
        Az.append(float(i[6]))
        
#new matrix, all data is not arranged in floats
Measurements=np.column_stack((Id, Xs, Xe, Ys, Ye, Le, Az))

   
def row_pick(a,b,c):
    azimuth_values=[]
    azimuth_indexes=[]
    if isinstance(c,list):
        for x,i in enumerate(c):
            if a < i <b:
                azimuth_values.append(i)
                azimuth_indexes.append(x)
        return azimuth_values, azimuth_indexes



####test#####
test=row_pick(8,140,Le)

j=test[1]

# print test
# print (" ")
# print ("the azimuths are"), test[0]
# print ("the locations of the azimuths in the measurments are"), test[1]
# print (" ")
final_values= [Measurements[i] for i in test[1]]  ######### inesrt inside the code

 
for i in final_values: ########### insert inside the code
    shorter_decimals=[]
    short_command=' '.join("%.2f" % value for value in i)
    shorter_decimals.append(short_command)
    print(shorter_decimals)


##test adding list 

# for x,y in zip(shorter_decimals, j):
#     q=[]
#     q.append(x)
#     q.append(y)
#     print q

# #print final_values
# print len(final_values)
# #print ' '.join("%.2f" % value for value in final_values)
# c= '' .join("%.2f" % value for value in final_values[0])
# #print final_values
# print(" ")
# print(" ")
# print type(final_values)
# #print final_values[1]
# print type(final_values[1])

# print(" ")
# g=final_values[1]
# print type(g)
 #print (type(g[1]))




