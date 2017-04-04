# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:50:09 2017

@author: bala635
"""

number = input("enter a number: ")
number = int(number)
total = 0

for i in range(1,number):
    if (i%3 == 0) or (i%5 == 0):
        total = total+i
        
print("sum of numbers from 1 to {} that are multiples of 3 or 5 is {}".format(number,total))