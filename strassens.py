#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:47:09 2018

@author: vogebr01
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:23:32 2018

@author: vogebr01
"""

import math
import random
import datetime
import sys

# for running script from command line
import argparse

# test strings ###################################################################################

#test = '2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1'

#testA = '0\n1\n' * 9

#test2 = '2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n\
#2\n3\n4\n5\n6\n7\n1\n2\n4\n9\n2\n3\n5\n4\n8\n9\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1\n5\n6\n7\n1\n2\n3\n4\n5\n6\n7\n1\n2\n4\n2\n3\n4\n5\n6\n7\n1'

##################################################################################################


# This helps with testing
def generate_string(num):
    out = ""
    for x in range(2 * num**2):
        out = out + str(random.randrange(-10, 10, 1)) + "\n"
    
    return out[:-1]   

# This turns a string of length 4n into two n x n matrices
def make_matrices(d, entry):
    mat = [[math.inf]*d for i in range(d)]
    mat1 = [[math.inf]*d for i in range(d)]
    splitted = entry.split('\n')
    for x in range(d):
        mat[x] = [int(x) for x in (splitted[:d**2][x*d:x*d+d])]
        mat1[x] = [int(x) for x in (splitted[d**2:][x*d:x*d+d])]
        
    return [mat, mat1]

# for adding matrices
def add_Mat(A, B):
    C = [[math.inf]*len(A) for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = int(A[i][j]) + int(B[i][j])
     
    return C    

# subtracting matrices   
def sub_Mat(A, B):
    C = [[math.inf]*len(A) for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = int(A[i][j]) - int(B[i][j])
     
    return C

# for returning the diagonals from the command line
def return_Diags(Mat):
    out = []
    i = 0
    #print("Here are the diagonals: ")
    for x in range(len(Mat)):
        out.append(Mat[x][i])
        i += 1
    for j in out:
        print(str(j) + '\n')
    #return(out)
        

# conventional algorithm for matrix multiplication
def conv(d, A, B):
    
    C = [[math.inf]*d for i in range(d)]
    
    for i in range(0,d):
        for j in range(0,d):
            C[i][j] = 0
            for k in range(0,d):
                C[i][j] += int(A[i][k])*int(B[k][j])
    return C

# Strassen's algorithm for matrix multiplication
def Stras(d, A, B, cut):
    
    
    # so we know whether to throw out some zeroes at the end
    hold = d
    
    # starting base case
    if d <= cut:
        return conv(d, A, B)

        
    # 0-padding    
    while d%2 != 0:
        A = [x + [0] for x in A]
        B = [x + [0] for x in B]
        A.append([])
        B.append([])
        A[d] = [0] * (d + 1)
        B[d] = [0] * (d + 1)
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
    
    P1 = Stras(int(d/2), X, sub_Mat(F, H), cut)
    P2 = Stras(int(d/2), add_Mat(X, Y), H, cut)
    P3 = Stras(int(d/2), add_Mat(Z, W), E, cut)
    P4 = Stras(int(d/2), W, sub_Mat(G, E), cut)
    P5 = Stras(int(d/2), add_Mat(X, W), add_Mat(E, H), cut)
    P6 = Stras(int(d/2), sub_Mat(Y, W), add_Mat(G, H), cut)
    P7 = Stras(int(d/2), sub_Mat(X, Z), add_Mat(E, F), cut)
    
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
            
            
     # determines whether to throw out zeroes
    if hold < d:
        FINAL = [x[:-1] for x in FINAL][:-1]
    
    return FINAL
            
######### testing #############################################################          

#print(Stras(4, make_matrices(4, test)[0], make_matrices(4, test)[1], 2))
#print("\n")
#print(Stras(3, make_matrices(3, testA)[0], make_matrices(3, testA)[1], 2))
#print("\n")
#print(Stras(6, make_matrices(6, test2)[0], make_matrices(6, test2)[1], 2))

#V = generate_string(25)
#W = make_matrices(25, V)
#Z = W[0]
#T = W[1]
#print(conv(25, Z, T) == Stras(25, Z, T, 2))

# Make sure Strassens is computing correctly ##################################

#for x in range(3, 210, 3):
#    A = make_matrices(x, generate_string(x))
#    print(conv(x, A[0], A[1]) == Stras(x, A[0], A[1], 4))

#============================== Generate timetrials ===========================

#for cut in [4, 8, 16, 32]:
#    for x in [4, 8, 10, 16, 25, 32, 50, 64, 100, 128, 200, 256, 355, 512]:
#        gen = []
#        for z in range(3):
#            matrices = make_matrices(x, generate_string(x))
#            stras_start = datetime.datetime.now()
#            Stras(x, matrices[0], matrices[1], cut)
#            stras_stop = datetime.datetime.now()
#            gen.append(stras_stop - stras_start)
#        print("CUT: ", cut, "DIM: ", x, "STRAS: ", (gen[0] + gen[1] + gen[2])/3)
# =============================================================================
    

# parse arguments for running Python script from command line

parser = argparse.ArgumentParser(description="Python Script for Conventional and Modified Strassen's Algorithm for Matrix Multiplication")
parser.add_argument('zero', help='flag', type=int, choices=[0])
parser.add_argument('dimension', help='dimension of matrix to be multiplied', type=int)
parser.add_argument('inputfile', help='input file as ASCII file', type=argparse.FileType('r'))
args = parser.parse_args()

if args.zero == 0:
    count = 0
    out = ''
    with open(args.inputfile.name) as userfile:
        lines = userfile.readlines()
        for i in lines:
            if i.strip('\n').strip() != '':
                count += 1
                out += i.strip('\n').strip() + '\n'
        if count != 2*args.dimension**2:
            print('Specified dimension mismatch with number of lines in ' + args.inputfile.name + ', please try again.')
            sys.exit()
        else:
            #print(out)
            matrices = make_matrices(args.dimension, out)
            #print(conv(args.dimension, matrices[0], matrices[1]))
            #print(Stras(args.dimension, matrices[0], matrices[1]))
            #print(return_Diags(conv(args.dimension, matrices[0], matrices[1])))
            return_Diags(Stras(args.dimension, matrices[0], matrices[1], 16))


