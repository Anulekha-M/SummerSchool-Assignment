# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:49:15 2021

@author: SAMIR_K_MAJUMDAR
"""

#Assignment 1

#Question 1
import numpy as np
#vector containing random numbers between 0,1
y_hat=np.random.random((100))
print (y_hat)
#vector containing 0𝑠 and 1s
y=np.random.randint(2, size=100)
print (y)

#Computing cross entropy loss function
n=100
O=0
for i in range (n):
    O=O+(b[i]*np.log2(a[i]))+((1-b[i])*np.log2(1-a[i]))
O=O*(-1/n)
print (O)

#**********************************************************

#Question 2

class Target:
   array=[10,20,10,40,50,60,70] 
   tar=50
   ans=dict([])

   index=1
   for i in range (len(array)):
       for j in range (len(array)):
           if array[i]+array[j]==tar:
               ans[(index)]=[i,j]
               index=index+1
                

c1=Target()
print('Following indices give sum of 50: ',c1.ans)