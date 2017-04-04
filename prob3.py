# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:59:55 2017

@author: bala635
"""
#def prnum(number):
#    n = 2
#    prime = 1
#    while (n < round(number/2)+1):
#        if number%n == 0:
#            prime = 0
#            break
#        else:
#            n = n+1
#    
#    return(prime)    
#
#
##from __future__ import division
#num = input("enter a number: ")
#num = int(num)
#primes = [];
#
#for i in range(2,round(num/2)+1):
#    if (prnum(i) == 1) and (num%i == 0):
#        primes.append(i)
#        
#print(max(primes))
        

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

number = input("enter a number: ")
pfs = prime_factors(int(number))
largest_prime_factor = max(pfs) 
print(largest_prime_factor)
