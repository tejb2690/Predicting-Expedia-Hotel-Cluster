# -*- coding: utf-8 -*-
"""


@author: hp
"""

"""
GENERATING 20000 INSTANCES FROM TRAIING SET WITH MISSING VALUES
IN FILE 'F20kwmiss.csv'



@author: hp
"""

import csv
fr = open('train.csv')
fw=open('F20kwmiss.csv','w')
writer=csv.writer(fw)
csv_f = csv.reader(fr)
k=1
for row in csv_f:

    if k==20001:
        break
    else:
       writer.writerow(row)
    k=k+1
fr.close()
fw.close()

""" SIMILARLY GENERATING 500 INSTANCES FROM TEST SET WITH MISSING VALUES
IN FILE 'F500wmiss_test.csv'"""


fr = open('test.csv')
fw=open('F500wmiss_test.csv','w')
writer=csv.writer(fw)
csv_f = csv.reader(fr)
k=1
for row in csv_f:

    if k==501:
        break
    else:
       writer.writerow(row)
    k=k+1
fr.close()
fw.close()

"""
                    FOR BOTH TRAINING AND TEST DATASET


FILE GENERATING RECORDS WITHOUT MISSING VALUES IN FILE 'nomisngval.csv'
WITH  11857 INSTANCES & 24 ATTRIBUTES FOR TRAINING SET

FILE GENERATING RECORDS WITHOUT MISSING VALUES IN FILE 'nomisngval.csv'
WITH  281 INSTANCES & 22 ATTRIBUTES FOR TEST DATA SET

@author: hp
"""
from pandas import read_csv
import numpy

dataset = read_csv('F20kwmiss.csv', header=None)
# mark zero values as missing or NaN
dataset = dataset.replace(0, numpy.NaN)
# drop rows with missing values
dataset.dropna(inplace=True)
# summarize the number of rows and columns in the dataset
print(dataset.shape)
#print(dataset)
dataset.to_csv('nomisngval.csv', sep=',')

"""FILE GENERATING RECORDS WITHOUT MISSING VALUES IN FILE 'nomisngval_test.csv'
WITH  281 INSTANCES & 22 ATTRIBUTES FOR TEST DATA SET"""

              
              
from pandas import read_csv
import numpy

dataset = read_csv('F500wmiss_test.csv', header=None)
# mark zero values as missing or NaN
dataset = dataset.replace(0, numpy.NaN)
# drop rows with missing values
dataset.dropna(inplace=True)
# summarize the number of rows and columns in the dataset
print(dataset.shape)
#print(dataset)
dataset.to_csv('nomisngval_test.csv', sep=',')

"""
TRAINING SET OF 10000 INSTANCES WITH NO MISSING VALUES & with 24 FEATURES

@author: hp
"""

import csv

fr = open('nomisngval.csv')
fw=open('train10k.csv','w')
writer=csv.writer(fw)
csv_f = csv.reader(fr)
k=0
for row in csv_f:
    if k==0:
        k=k+1
        continue
    else:
        if k==10003:
            break
        else:           
            writer.writerow(row)
            k=k+1
  
fr.close()
fw.close()



import csv

fr = open('nomisngval_test.csv')
fw=open('test50.csv','w')
writer=csv.writer(fw)
csv_f = csv.reader(fr)
k=0
for row in csv_f:
    if k==0:
        k=k+1
        continue
    else:
        if k==53:
            break
        else:           
            writer.writerow(row)
            k=k+1
  
fr.close()
fw.close()


"""
CORELLATION BETWEEN ATTRIBUTES IN TRAINING SET

@author: hp
"""

import pandas 
import numpy
data = pandas.read_csv("train10k.csv")
        
for loop1 in range(2, 23): #loop1= 2 to 22 as colno 0 is serial no,col1,col12,col13 are dates. col24 is cluster no 
         if((loop1==12) or (loop1==13)):
             continue
         for loop2 in range(loop1+1,24 ):#loop2= loop1+1 to 23
            if((loop2==12) or (loop2==13)):
                 continue
            print "coreelation between attribute no %d and %d " %(loop1,loop2) 
            print numpy.corrcoef(data.iloc[:,(loop1)],data.iloc[:,(loop2)])
            

print "CORELLATION BETWEEN ATTRIBUTES SHOWN"  
print "GROUP OF HOTEL CLUSTERS YET TO BE SHOWN "          

"""                                     FOR TRAINING SET                    

                            ELIMINATING COLUMNS WITH STRING VALUED ATTRIBUTES 
"""
import csv
"""   
with open("train10k.csv","r") as source:
    rdr= csv.reader( source )
    with open("rmcoltrain10kwithatt.csv","w") as result1:
        wtr1= csv.writer( result1 )
        #k=0
        for r in rdr:
            wtr1.writerow( (r[2],r[3],r[4], r[5], r[6], r[7], r[8], r[9], r[10],r[11], r[14], r[15], r[16],r[17], r[18], r[21], r[22],r[23],r[24]) )
source.close()
"""

with open("train10k.csv","r") as source:
    rdr= csv.reader( source )
    with open("rmcoltrain10knoatt.csv","w") as result1:
        wtr1= csv.writer( result1 )
        k=0
        for r in rdr:
            if(k==0):
                k=k+1
                continue
            else:
                wtr1.writerow( (r[2],r[3],r[4], r[5], r[6], r[7], r[8], r[9], r[10],r[11], r[14], r[15], r[16],r[17], r[18], r[21], r[22],r[23],r[24]) )
                k=k+1
source.close()
result1.close()   

            
"""                                     FOR TEST SET                    

                            ELIMINATING COLUMNS WITH STRING VALUED ATTRIBUTES 
"""                


"""

with open("test50.csv","r") as source:
    rdr= csv.reader( source )
    with open("rmcoltest50withatt.csv","w") as result1:
        wtr1= csv.writer( result1 )
        #k=0
        for r in rdr:
            wtr1.writerow( (r[3],r[4], r[5], r[6], r[7], r[8], r[9], r[10],r[11], r[12], r[15], r[16],r[17], r[18], r[19], r[20],r[21],r[22]) )
source.close()

"""

            
            
            
with open("test50.csv","r") as source:
    rdr= csv.reader( source )
    with open("rmcoltest50noatt.csv","w") as result1:
        wtr1= csv.writer( result1 )
        k=0
        for r in rdr:
            if(k==0):
                k=k+1
                continue
            else:
                wtr1.writerow( (r[3],r[4], r[5], r[6], r[7], r[8], r[9], r[10],r[11], r[12], r[15], r[16],r[17], r[18], r[19], r[20],r[21],r[22]) )
                k=k+1
source.close()
result1.close()

"""
            FINDING K-NEAREST NEIGHBOR FOR EACH TEST INSTANCES
            IN THIS PROGRAM, K IS A VARIABLE. YOU CAN CHANGE THE VALUES OF K AND FIND DIFFERENT SIZED HOTEL CLUSTER GROUPINGS

@author: hp
"""
	
import math
def uclideandistaence(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)



import operator 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = uclideandistaence(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
	


     
     

import csv 
def get_data(filename):
    with open(filename, 'r') as f: 
        #reader = csv.reader(f)       
        testset = list(list(rec) for rec in csv.reader(f, delimiter=',')) #reads csv into a list of lists
        test_data=[]
        for list_i in testset:
            tmp = []
            for element in  list_i:
                tmp.append(float(element))
            test_data.append(tmp)
    return test_data
    


#get training data
train_data = get_data('rmcoltrain10knoatt.csv')

#get testing data
test_data = get_data('rmcoltest50noatt.csv')

k=1 #Change the value of K to get k predicted cluster(s) for each test instances
nei_clust_arr=[] 
for i in range(0,50):
    neighbors = getNeighbors(train_data,test_data[i][0:18],k )
    nei_clust_arr.append(neighbors)
for i in range(0,50):
    print "Group of %d hotel cluster(s) number(s) for %d th test instance" %(k,i)
    for j in range(0,k):
        print(nei_clust_arr[i][j][18:19])
                        
