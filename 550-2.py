#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:23:32 2018

@author: vogebr01
"""

import math
import random
import datetime

# test strings

test = '2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1'

testA = '0\n1\n' * 9

test2 = '2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1'

def generate_string(num):
    out = ""
    for x in range(2 * num**2):
        out = out + str(random.randrange(-10, 10, 1)) + "\n"
    
    return out[:-1]      


# turns a matrix into a string to be inputted to one of the functions 
def build_string(A):
    out = ""
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            out = out + str(A[i][j]) + "\n"
            
    # get rid of the last \n
    
    return out[:-1]

# for adding matrices

def add_Mat(A, B):
    C = [[math.inf]*len(A) for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = str(int(A[i][j]) + int(B[i][j]))
     
    return C    

# subtracting matrices   

def sub_Mat(A, B):
    C = [[math.inf]*len(A) for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = str(int(A[i][j]) - int(B[i][j]))
     
    return C

# conventional algorithm for matrix multiplication
def conv(d, line):
    A = [[math.inf]*d for i in range(d)]
    B = [[math.inf]*d for i in range(d)]
    C = [[math.inf]*d for i in range(d)]
    
    splitted = line.split('\n')
    
    for x in range(0,d):
        A[x] = splitted[:d**2][x*d:x*d+d]
        B[x] = splitted[d**2:][x*d:x*d+d]
    
    for i in range(0,d):
        for j in range(0,d):
            C[i][j] = 0
            for k in range(0,d):
                C[i][j] += int(A[i][k])*int(B[k][j])
    return C

# Strassen's algorithm for matrix multiplication
def Stras(d, line):
    
    # starting base base
    if d <= 4:
        return conv(d, line)
    
    A = [[math.inf]*d for i in range(d)]
    B = [[math.inf]*d for i in range(d)]
    
    splitted = line.split('\n')
    
    for x in range(0,d):
        A[x] = splitted[:d**2][x*d:x*d+d]
        B[x] = splitted[d**2:][x*d:x*d+d]
        
    # 0-padding
        
    #while math.log2(d).is_integer() == False:
    #    A = [x + ['0'] for x in A]
    #    B = [x + ['0'] for x in B]
    #    A.append([])
    #    B.append([])
    #    A[d] = ['0'] * (d + 1)
    #    B[d] = ['0'] * (d + 1)
    #    d += 1
    
    while d%2 != 0:
        A = [x + ['0'] for x in A]
        B = [x + ['0'] for x in B]
        A.append([])
        B.append([])
        A[d] = ['0'] * (d + 1)
        B[d] = ['0'] * (d + 1)
        d += 1   
        
    # initiate the result-matrix
    
    FINAL = [[math.inf]*d for i in range(d)]
    
    # calculations on calculations
        
    X = [x[0:int(len(x)/2)] for x in A[0:int(len(A)/2)]]
    Y = [x[int(len(x)/2):] for x in A[0:int(len(A)/2)]]
    Z = [x[0:int(len(x)/2)] for x in A[int(len(A)/2):]]
    W = [x[int(len(x)/2):] for x in A[int(len(A)/2):]]
    
    E = [x[0:int(len(x)/2)] for x in B[0:int(len(B)/2)]]
    F = [x[int(len(x)/2):] for x in B[0:int(len(B)/2)]]
    G = [x[0:int(len(x)/2)] for x in B[int(len(B)/2):]]
    H = [x[int(len(x)/2):] for x in B[int(len(B)/2):]]
    
    P1 = Stras(int(d/2), (build_string(X) + "\n" + build_string(sub_Mat(F, H))))
    P2 = Stras(int(d/2), (build_string(add_Mat(X, Y)) + "\n" + build_string(H)))
    P3 = Stras(int(d/2), (build_string(add_Mat(Z, W)) + "\n" + build_string(E)))
    P4 = Stras(int(d/2), (build_string(W) + "\n" + build_string(sub_Mat(G, E))))
    P5 = Stras(int(d/2), (build_string(add_Mat(X, W)) + "\n" + build_string(add_Mat(E, H))))
    P6 = Stras(int(d/2), (build_string(sub_Mat(Y, W)) + "\n" + build_string(add_Mat(G, H))))
    P7 = Stras(int(d/2), (build_string(sub_Mat(X, Z)) + "\n" + build_string(add_Mat(E, F))))
    
    XE_YG = add_Mat(sub_Mat(add_Mat(P5, P4), P2), P6)
    ZE_WG = add_Mat(P3, P4)
    XF_YH = add_Mat(P1, P2)
    ZF_WH = sub_Mat(sub_Mat(add_Mat(P5, P1), P3), P7)
    
    # fill in the result matrix
    
    for i in range(int(d/2)):
        for j in range(int(d/2)):
            FINAL[i][j] = XE_YG[i][j]
            
    for i in range(int(d/2)):
        for j in range(int(d/2)):
            FINAL[i+int(d/2)][j] = ZE_WG[i][j]
            
    for i in range(int(d/2)):
        for j in range(int(d/2)):
            FINAL[i][j+int(d/2)] = XF_YH[i][j]
            
    for i in range(int(d/2)):
        for j in range(int(d/2)):
            FINAL[i+int(d/2)][j+int(d/2)] = ZF_WH[i][j]
            
    return FINAL
            
            

#print(Stras(4, test))
#print("\n")
#print(Stras(3, testA))
#print("\n")
#print(Stras(6, test2))


for x in range(100, 200, 10):
    reg_start = datetime.datetime.now()
    conv(x, generate_string(x))
    reg_stop = datetime.datetime.now()
    print(x, "REG: ", reg_stop - reg_start)
    
    stras_start = datetime.datetime.now()
    Stras(x, generate_string(x))
    stras_stop = datetime.datetime.now()
    print(x, "STRAS: ", stras_stop - stras_start)
    



