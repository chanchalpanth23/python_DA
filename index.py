import numpy as np

import time
import math


# print(np.array([1,2,3]))
# #array
# #zeroes

# arr1= np.ones(10)
# print(arr1.dtype) 

# arr1=np.arange(1,10,2)
# print(arr1)

# print(np.zeros((3,3)))

# arr2=np.random.random(5)
# print(arr2)

# #floor-> decimal part ko remove krke integer ko return krne
# arr2=np.floor(np.random.random(5)*100)
# print(arr2)

# arr2= np.linspace(1,10,5)
# print(arr2)


# ar1=np.array([[1,2,3],[4,5,6]])            #(2,3) 2->row or 3->column
# print(ar1.shape)
# ar2=ar1.reshape
# print(ar1.size)                            #6->no. of elements
# print(ar1.ndim)

#arr+arr

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr3= np.concatenate((arr1,arr2))  #to merge multiple arrays.(tuple mei)
# print(arr3)

# arr1= np.array([[1,2,3,4],
#                [5,6,7,8]])
# arr2= arr1[0:1,-1:-3:-1]  
# print(arr2)


# arr2= arr1[0:1,2:3]
# print(arr2)
arr1=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# arr2=arr1[1:3,0:2]
# print(arr2)

# arr2=arr1[:,::2]
# print(arr2)

# print(arr1[:,-1 :-2:-2])
# print(arr1[:,-1 :-4:-2])
# print(arr1[0:4,2:3])

# max-> 0=columnwise,1=rowwise
# maxval=np.max(arr1,axis=0)
# print(maxval)
# maxval=np.max(arr1,axis=1)
# print(maxval)
# maxval=np.max(arr1)
# print(maxval)

# arr1=np.array([1,2,3,10])
# print(int(np.mean(arr1)))
# print(int(np.median(arr1)))
# maxval=np.max(arr1,axis=1)
# print(maxval)
# maxval=np.max(arr1,axis=0)
# print(maxval)

#argmax->index find for max value
# print(np.argmax(arr1))
#standard deviation
#1.mean
#2. mean-every element
#3. squares then mean
#4. sq.route
arr=np.array([5,6,2,9])

# def mean():
#     mean=len()
#     for i in mean(1,2):
#         for i in arr:
#             total=1
# def average(arr):
#     s=0
#     n=len(arr)
#     for i in arr:
#         s+=1
#         return s/n
# def std(arr):
#     avg=average(arr)
#     list=[]
#     for i in arr:
#         s=i-avg
#         a=s**2
#         list.append(a)
#     arr1=np.array(list)
#     return(average(arr1))**0.5
# m=np.array([1,2,3,4])
# print(std(m))


# print(np.std(arr1))
# x=(int(np.mean(arr1)))
import numpy as np


#hstack # vstack
# vstack-> vertically merge
# hstack-> horizontally merge
# a1= np.array([1,2,3])
# a2= np.array([4,5,6])
# a3=np.vstack((a1,a2))
# print(a3)
# a3=np.hstack((a1,a2))
# print(a3)

#BOOLEAN MASKING
# a1=np.array([1,2,3,4,5,6,7,8,9])
# a2=a1[a1%2==0]   
# a2= a1[a1%2!=0]   
# print(a2)

# dot product-> equivalent postion ka product then add
# a1=np.array([1,2,3])                  1*4+2*5+3*6=32
# a2=np.array([4,5,6])
# a3=np.dot(a1,a2)
# print(a3)

#matrix multiplication
# a1= np.array([[4,5],[2,2]])       
# a2= np.array([[2,2],[1,2]])     
# a3=np.matmul(a1,a2)
# print(a3)
# print(a1@a2)

#TRANPOSE-> row ko column or column ko row m convert krne ke liye
# a2=np.array([4,5])
# print(a2.T)

#DETERMINANT->cross product ko subtract krna 
# [a b]
# [c d]
# ad-cb
# a1= np.array([[1,2],[3,4]])
# a2= np.array([[5,6],[7,8]])
# determinant= int(np.linalg.det(a2))
# print(determinant)

#RANGE MASKING
# a1=np.array([1,2,3,4,5,6,7,8,])
# a2=a1[(a1>3) & (a1<6)]
# print(a2)

#REPLACEMENT MASKING
# a1=np.array([1,2,3,4,5,6,7])
# a1[a1>4]=100
# print(a1)


# a1=np.array([[1,3],[4,5]])
# a2=np.array([[5,4],[2,3]])
# determinant=int(np.linalg.det(a1))
# print(determinant)

#CONDITIONAL FILTERING
# arr1=np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr1[arr1>=5])

#mathematical operations
# arr=np.array([1,2,3,4,5])
# arr1=np.array([2,3,4,5,6])
# arr=arr+arr1
# print(arr)
# arr=arr+5
# arr=arr-5
# arr=arr*2
# print(arr)

# arr=np.array([1,4,9,16,25])
# arr=np.sqrt(arr)
# print(arr)