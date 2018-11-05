#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:44:56 2018

@author: vogebr01
"""

# Sees how many Fibonacci numbers can be computed in one minute using the 
# matrix algorithm defined in class

import time

def Matrix_Fib(n):
    if n == 0:
        return(0)
        
    elif n == 1:
        return(1)
        
    else:
        helper = [[0, 1], [1, 1]]
        
        helperA = [[0, 1], [1, 1]]
 
# n-2 to take care of Python's indexing strategy, and 
# the fact that the algorithm produces the (x + 1)th iteration
# each time through, since we start with helper^1
        if (n-2) % 2 == 0:
        
            for x in range(int((n-2)/2)):
                tL = helper[0][0] * helperA[0][0] + helper[0][1] * helperA[1][0]
                tR = helper[0][0] * helperA[0][1] + helper[0][1] * helperA[1][1]
                bL = helper[1][0] * helperA[0][0] + helper[1][1] * helperA[1][0]
                bR = helper[1][0] * helperA[0][1] + helper[1][1] * helperA[1][1]
            
                helper = [[tL, tR], [bL, bR]]
 
# square it        
            tL = helper[0][0] * helper[0][0] + helper[0][1] * helper[1][0]
            tR = helper[0][0] * helper[0][1] + helper[0][1] * helper[1][1]
            bL = helper[1][0] * helper[0][0] + helper[1][1] * helper[1][0]
            bR = helper[1][0] * helper[0][1] + helper[1][1] * helper[1][1]
        
            helper = [[tL, tR], [bL, bR]]
        
        
            return([helper[0][0], helper[1][0]][0])
 
# Same as the first loop, but this time I square it then multiply it by helper again           
        else:
            for x in range(int((n-2)//2)):
                tL = helper[0][0] * helperA[0][0] + helper[0][1] * helperA[1][0]
                tR = helper[0][0] * helperA[0][1] + helper[0][1] * helperA[1][1]
                bL = helper[1][0] * helperA[0][0] + helper[1][1] * helperA[1][0]
                bR = helper[1][0] * helperA[0][1] + helper[1][1] * helperA[1][1]
            
                helper = [[tL, tR], [bL, bR]]
                
            tL = helper[0][0] * helper[0][0] + helper[0][1] * helper[1][0]
            tR = helper[0][0] * helper[0][1] + helper[0][1] * helper[1][1]
            bL = helper[1][0] * helper[0][0] + helper[1][1] * helper[1][0]
            bR = helper[1][0] * helper[0][1] + helper[1][1] * helper[1][1]
                
            helper = [[tL, tR], [bL, bR]]
            
            tL = helper[0][0] * helperA[0][0] + helper[0][1] * helperA[1][0]
            tR = helper[0][0] * helperA[0][1] + helper[0][1] * helperA[1][1]
            bL = helper[1][0] * helperA[0][0] + helper[1][1] * helperA[1][0]
            bR = helper[1][0] * helperA[0][1] + helper[1][1] * helperA[1][1]
            
            helper = [[tL, tR], [bL, bR]]            
            
            return([helper[0][0], helper[1][0]][0])


#################################################

# Everything's the same, except the arithmetic is modulo 2^16
def mod_Matrix_Fib(n):
    if n == 0:
        return(0)
        
    elif n == 1:
        return(1)
        
    else:
        helper = [[0, 1], [1, 1]]
        
        helperA = [[0, 1], [1, 1]]
        
        if (n-2) % 2 == 0:
        
            for x in range(int((n-2)/2)):
                tL = (helper[0][0] * helperA[0][0])%65536 + (helper[0][1] * helperA[1][0])%65536
                tR = (helper[0][0] * helperA[0][1])%65536 + (helper[0][1] * helperA[1][1])%65536
                bL = (helper[1][0] * helperA[0][0])%65536 + (helper[1][1] * helperA[1][0])%65536
                bR = (helper[1][0] * helperA[0][1])%65536 + (helper[1][1] * helperA[1][1])%65536
            
                helper = [[tL, tR], [bL, bR]]
         
            tL = (helper[0][0] * helper[0][0])%65536 + (helper[0][1] * helper[1][0])%65536
            tR = (helper[0][0] * helper[0][1])%65536 + (helper[0][1] * helper[1][1])%65536
            bL = (helper[1][0] * helper[0][0])%65536 + (helper[1][1] * helper[1][0])%65536
            bR = (helper[1][0] * helper[0][1])%65536 + (helper[1][1] * helper[1][1])%65536
        
            helper = [[tL, tR], [bL, bR]]
        
        
            return([helper[0][0], helper[1][0]][0])
            
        else:
            for x in range(int((n-2)//2)):
                tL = (helper[0][0] * helperA[0][0])%65536 + (helper[0][1] * helperA[1][0])%65536
                tR = (helper[0][0] * helperA[0][1])%65536 + (helper[0][1] * helperA[1][1])%65536
                bL = (helper[1][0] * helperA[0][0])%65536 + (helper[1][1] * helperA[1][0])%65536
                bR = (helper[1][0] * helperA[0][1])%65536 + (helper[1][1] * helperA[1][1])%65536
            
                helper = [[tL, tR], [bL, bR]]
         
            tL = (helper[0][0] * helper[0][0])%65536 + (helper[0][1] * helper[1][0])%65536
            tR = (helper[0][0] * helper[0][1])%65536 + (helper[0][1] * helper[1][1])%65536
            bL = (helper[1][0] * helper[0][0])%65536 + (helper[1][1] * helper[1][0])%65536
            bR = (helper[1][0] * helper[0][1])%65536 + (helper[1][1] * helper[1][1])%65536
        
            helper = [[tL, tR], [bL, bR]]
        
        
            tL = (helper[0][0] * helperA[0][0])%65536 + (helper[0][1] * helperA[1][0])%65536
            tR = (helper[0][0] * helperA[0][1])%65536 + (helper[0][1] * helperA[1][1])%65536
            bL = (helper[1][0] * helperA[0][0])%65536 + (helper[1][1] * helperA[1][0])%65536
            bR = (helper[1][0] * helperA[0][1])%65536 + (helper[1][1] * helperA[1][1])%65536
            
            helper = [[tL, tR], [bL, bR]]            
            
            return([helper[0][0], helper[1][0]][0])

#################################################

def main():
    starter = 1

    stop = time.time() + 60

    while time.time() < stop:
        Matrix_Fib(starter)
        starter += 1
    
    print("Regular matrix Fib. made it to: ", starter)

    starter1 = 1

    stop1 = time.time() + 60

    while time.time() < stop1:
        mod_Matrix_Fib(starter1)
        starter1 += 1
    
    print("Matrix Fib. modulo 2^16 made it to: ", starter1)

main()     
        
    