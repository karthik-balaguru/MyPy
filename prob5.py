# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:26:54 2017

@author: bala635
"""

def factors(num):
    num = int(num)
    n = 2
    faclist = []
    while (n <= num):
        if num%n == 0:
            faclist.append(n)
            num = num/n
            n = 2
        else:
            n = n+1
    
    return(faclist)

#num = input("enter a number: ") 
#faclist = factors(num)       
#print(faclist)

import numpy as np            
    
primes = np.array([2, 3, 5, 7, 11, 13, 17, 19])

list1 = np.zeros(8)

n = 2
while (n<=20):
    print(n)
    templist = factors(n)
    #print(templist)
    m = len(templist)
    list2 = np.zeros(8)
    for i in range(0,m):
        p = templist[i]
        if p==2:
            list2[0] = list2[0]+1
        elif p==3:
            list2[1] = list2[1]+1
        elif p==5:
            list2[2] = list2[2]+1
        elif p==7:
            list2[3] = list2[3]+1
        elif p==11:
            list2[4] = list2[4]+1
        elif p==13:
            list2[5] = list2[5]+1
        elif p==17:
            list2[6] = list2[6]+1
        else:
            list2[7] = list2[7]+1
               
        #print(list2)
            
    for i in range(0,8):
        list1[i] = max(list1[i],list2[i])
        
    n = n+1
        
prod = 1
for i in range(0,8):
    prod = prod*(primes[i]**list1[i])
    
print(prod)
    
             
    
