# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:09:05 2017

@author: bala635
"""
fib = [1, 2]
n = 1

while (int(fib[n-1]) + int(fib[n]) < 4000000):
    temp = int(fib[n-1]) + int(fib[n])
    fib.append(temp)
    n = n+1

num = len(fib)
total = 0

for i in range(0,num):
    if (fib[i]%2 == 0):
        total = total + fib[i]
        
print("Sum of fibonacci numbers under 4 million that are even is: {}".format(total))