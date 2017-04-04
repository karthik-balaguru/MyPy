# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 02:31:12 2017

@author: bala635
"""

def sumofsquares(num):
    n = 1
    sum1 = 0
    while (n<=num):
        sum1 = sum1 + n**2
        n = n+1
    return(sum1)
    
def squareofsum(num):
    n = 1
    sum2 = 0
    while (n<=num):
        sum2 = sum2 + n
        n = n+1
    sum2 = sum2**2
    return(sum2)
    
num = input("enter a number: ") 
num = int(num)   
diffsum = squareofsum(num) - sumofsquares(num)
print(diffsum)
        