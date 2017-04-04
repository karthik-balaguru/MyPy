# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 02:41:21 2017

@author: bala635
"""

def prime(num):
    n = 1
    m = 2
    while (m < num):
        if (num%m == 0):
            n = 0
            break
        else:
            m = m+1
            
    return(n)
            
count = 0
n = 2

primelist = []
while (count < 10002):
    p = prime(n)
    if p == 1:
        count = count+1
        print(count)
        primelist.append(n)
    n = n+1
    
print(primelist[10000])
     