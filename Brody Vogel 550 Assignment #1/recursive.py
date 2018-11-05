#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:36:40 2018

@author: vogebr01
"""

# Sees how many Fibonacci numbers can be computed in one minute using the 
# recursive algorithm defined in class

import time

def Dumb_Fib(n):
    if n == 0:
        return(0)
    
    elif n == 1:
        return(1)
    
    else:
        return(Dumb_Fib(n - 2) + Dumb_Fib(n - 1))

#################################

def mod_Dumb_Fib(n):
    if n == 0:
        return(0)
    
    elif n == 1:
        return(1)
    
    else:
        return((mod_Dumb_Fib(n-1) + mod_Dumb_Fib(n-2))%65536)

#################################

def main():
    starter = 1

    stop = time.time() + 60

    while time.time() < stop:
        Dumb_Fib(starter)
        starter += 1
    
    print("Regular recursive Fib. made it to: ", starter)

    starter1 = 1

    stop1 = time.time() + 60

    while time.time() < stop1:
        mod_Dumb_Fib(starter1)
        starter1 += 1
    
    print("Recursive Fib. modulo 2^16 made it to: ", starter1)
    
main()