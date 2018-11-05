#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:07:30 2018

@author: vogebr01
"""

# Sees how many Fibonacci numbers can be computed in one minute using the 
# iterative algorithm defined in class

import time

def Smarter_Fib(n):
    A = []
    
    A.append(0)
    A.append(1)
    
    for i in range(2, n):
        A.append(A[i - 2] + A[i - 1])
    
    return(A[n-1])

#################################################

def mod_Smarter_Fib(n):
    A = []
    
    A.append(0)
    A.append(1)
    
    for i in range(2, n):
        A.append((A[i-1] + A[i-2])%65536)
    
    return(A[n-1])

#################################################

def main():
    starter = 1

    stop = time.time() + 60

    while time.time() < stop:
        Smarter_Fib(starter)
        starter += 1
    
    print("Regular iterative Fib. made it to: ", starter)
    
    starter1 = 1

    stop1 = time.time() + 60

    while time.time() < stop1:
        mod_Smarter_Fib(starter1)
        starter1 += 1
    
    print("Iterative fib modulo 2^16 made it to: ", starter1)
    
main()