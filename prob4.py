# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:09:21 2017

@author: bala635
"""
palin = []

for i in range(100,1000):
    for j in range(100,1000):
        
        prod = str(i*j)
        lenstr = len(prod)
        list1 = []
        
        for k in range(0,lenstr):
            list1.append(prod[k])
        
        list2 = list1[::-1]
        
        if (list1 == list2):
            palin.append(i*j)
            
print(max(palin))
        
    
            
            
        
        