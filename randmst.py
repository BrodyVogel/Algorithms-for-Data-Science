#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:17:49 2018

@author: vogebr01
"""

# for the graphs
import random
import itertools
import math

# for testing and plots
# import matplotlib.pyplot as plt
import datetime

# for running script from command line
import argparse


# Define an Edge for each of the 4 parts of the assignment. 
# Each edge has a (left, right) component and a corresponding weight.
# We also gave each edge an output() method so we could better test them.

# dim = 0
class Edge1:
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.weight = random.uniform(0,1)
        
    def output(self):
        return((self.left, self.right, self.weight))

# dimension = 2, in which the weights become Euclidean distance       
class Edge2:
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.weight = round(((right[1] - left[1])**2 + (right[0] - left[0])**2)**(1/2), 4)
        
    def output(self):
        return((self.left, self.right, self.weight))

# dim = 3        
class Edge3:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.weight = round(((right[1] - left[1])**2 + (right[0] - left[0])**2 + (right[2] - left[2])**2)**(1/2), 4)
        
    def output(self):
        return((self.left, self.right, self.weight)) 

# dim = 4      
class Edge4:

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.weight = round(((right[1] - left[1])**2 + (right[0] - left[0])**2 + (right[2] - left[2])**2 + (right[3] - left[3])**2)**(1/2), 4)
        
    def output(self):
        return((self.left, self.right, self.weight)) 

# Define a Graph for each part of the assignment. Each graph is composed of a (V, E)
# set of nodes and edges as defined in the classes above.
# The built-in itertools.combinations seemed fitting as a method to build the 
# edges since the graphs are complete and undirected.
# We rounded the random uniform numbers to 4 decimal points in the higher dimensions due to
# an issue with the random number generator that is discussed in the write-up. 

# dimension = 0
class Graph1:  
    
    def __init__(self, V):
        self.V = [i for i in range(V)]
        self.E = [Edge1(x[0], x[1]) for x in itertools.combinations(self.V, 2)]

# dim = 2, in which the nodes become points in the unit square                 
class Graph2:
   
    def __init__(self, V):
        self.V = [(round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 4)) for i in range(V)]
        self.E = [Edge2(x[0], x[1]) for x in itertools.combinations(self.V, 2)]

# dim 3, in which the nodes become points in the unit cube        
class Graph3:
   
    def __init__(self, V):
        self.V = [(round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 3)) for i in range(V)]
        self.E = [Edge3(x[0], x[1]) for x in itertools.combinations(self.V, 2)]

# dim 4, in which the nodes become points in the unit hypercube          
class Graph4:
   
    def __init__(self, V):
        self.V = [(round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 3), round(random.uniform(0, 1), 3)) for i in range(V)]
        self.E = [Edge4(x[0], x[1]) for x in itertools.combinations(self.V, 2)]                   

# pseudo-Adjacency-List for storing our edges, E; this saves time on the look-ups
# initializes in O(E); returns the neighbors of a node in O(1)        
def Adjacency_List(Graph):
    A = {key:[] for key in Graph.V}
    
    for edge in Graph.E:
        A[edge.right].append(edge)
        A[edge.left].append(edge)

    return(A)

# delete-min operation for getting the node from with lowest priority (smallest dist[v]) 
# from the pseudo-queue we're using
# it finds the index of the smallest priority in the queue, then pops that value
# runs around O(1)
def delete_min(queue):
    node = min(queue, key = lambda x: x[1])
    spot = queue.index(node)
    return(queue.pop(spot))

# change operation for updating the priority of nodes in the forthcoming algorithm
# it too finds the index of the wanted element and assigns it a new, specified priority 
# runs around O(1)
def change(queue, element, priority):
    spot= queue.index(element)
    queue[spot] = (element[0], priority)

# this is a method of throwing out edges with weights that will almost certainly not need to be used
# it speeds up the iterations considerably
# we found these numbers based on extensive trial and error; we think they're associated with the
# probabilities of a Uniform(0,1) distribution - discussed in the write-up    

cutoff_dict = {}
cutoff_dict[Graph1] = [.1, .03, .01, .0085, .006, .0045, .0035, .0025, .002, .0015]
cutoff_dict[Graph2] = [.25, .15, .1, .07, .07, .07, .07, .07, .06, .06, .06, .05]
cutoff_dict[Graph3] = [.32, .22, .19, .17, .16, .14, .12, .12, .11, .11]

cutoff_dict = {}
cutoff_dict[1] = [1.5, 1.5, 1.5, 1.5]
cutoff_dict[100] = [.1, .25, .32, .52]
cutoff_dict[500] = [.03, .15, .22, .35]
cutoff_dict[1000] = [.01, .1, .19, .32]
cutoff_dict[1500] = [.0085, .07, .17, .28]
cutoff_dict[2000] = [.006, .07, .16, .26]
cutoff_dict[2500] = [.0045, .07, .14, .25]
cutoff_dict[3000] = [.0035, .07, .12, .23]
cutoff_dict[4000] = [.0025, .07, .12, .22]
cutoff_dict[5000] = [.002, .06, .11, .2]
cutoff_dict[10000] = [.0015, .05, .11, .2]

           
# our implementation of Prim's Algorithm for finding the weight of a MST of a graph        
def Prims(Graph, source):
    # initialize prev and dist appropriately
    prev = {key:None for key in Graph.V}        
    dist = {key:math.inf for key in Graph.V}    
    dist[source] = 0                              
    
    
    # initialize X, a subset of a MST of the graph; and S to keep track of the nodes in X
    X = []
    S = []
    
    # initialize our "priority queue", H, which is a list that we've built the needed functions
    # for above
    H = [(v, dist[v]) for v in Graph.V]         
    
    
    # this chunk references the edges that are probably "safe" to throw out, as explained above
    # and in the write-up
    indexer = 1
    
    if len(Graph.V) >= 100:
        indexer = 100
    elif len(Graph.V) >= 500:
        indexer = 500
    elif len(Graph.V) >= 1000:
        indexer = 1000
    elif len(Graph.V) >= 1500:
        indexer = 1500
    elif len(Graph.V) >= 2000:
        indexer = 2000
    elif len(Graph.V) >= 2500:
        indexer = 2500
    elif len(Graph.V) >= 3000:
        indexer = 3000
    elif len(Graph.V) >= 4000:
        indexer = 4000
    elif len(Graph.V) >= 5000:
        indexer = 5000
    elif len(Graph.V) >= 10000:
        indexer = 10000
        
    if type(Graph) == Graph1:
        Graph.E = [x for x in Graph.E if x.weight < cutoff_dict[indexer][0]]
    elif type(Graph) == Graph2:
        Graph.E = [x for x in Graph.E if x.weight < cutoff_dict[indexer][1]]        
    elif type(Graph) == Graph3:
        Graph.E = [x for x in Graph.E if x.weight < cutoff_dict[indexer][2]]   
    else:
        Graph.E = [x for x in Graph.E if x.weight < cutoff_dict[indexer][3]]            
    
    # creates the adjacency list for neighbors look-ups O(E)
    A = Adjacency_List(Graph)
        
    # while there are still nodes to deal with in H
    while H != []:
        # call to our delete_min operation O(1); v[0] gives the actual node, v
        v = delete_min(H)
        
        # add edge (prev[v], v) to X O(1); need all the conditions because the graph is undirected
        X.append([edge for edge in A[v[0]] if (edge.left == prev[v[0]] or edge.right == prev[v[0]]) and 
                                                 (edge.left == v[0] or edge.right == v[0])])

        # all the edges containing v that have not already been considered   
        v_edges = [x for x in A[v[0]] if (x.right not in S and x.left not in S)]
        
        # now v has been considered
        S.append(v[0])
        
        # go through all the edges containing v
        for edge in v_edges:
            # because of the way we implemented edges, we need to determine which end of the edge
            # is v, and then only consider the other end
            if v[0] == edge.right:
                where = edge.left
            else:
                where = edge.right
            
            # update the shortest path to the neighbor of v, if warranted; the abs() is to deal
            # with a funky error the random number generator threw
            if dist[where] > abs(edge.weight):
                hold = dist[where]
                dist[where] = abs(edge.weight)
                prev[where] = v[0]
            # call our defined change() to do the updating; the try/except is again to deal with
            # an issue from the random number generator
                try:
                    change(H, (where, hold), dist[where])
                except:
                    change(H, (where, math.inf), dist[where])
    
    # return the weight of the MST
    sums = 0
    for edge in X[1:]:
    # again need abs() to deal with the same issue as above
        sums = sums + abs(edge[0].weight)
    return(sums)

# the numbers we want to test our algorithm on
# test_numbers = [2, 16, 32, 64, 128, 256, 512, 1024, 1500, 2048, 2500, 3000, 3500, 4096, 
#                 4500, 5000, 6000, 7000, 8192, 12000, 16384]

# the tests, with times, that averages five runs through each size of n, for each type of graph
# code for plots is also included, although these aren't Python standard

# dimension = 0
# =============================================================================
# x1 = []
# y1 = []
# 
# for i in test_numbers:
#     x1.append(i)
#     G = Graph2(i)
#     hold = []
#     for z in range(1):
#         time = datetime.datetime.now()
#         random.seed(random.uniform(0,1000))
#         push = Prims(G, G.V[0])
#         hold.append(push)
#         print(datetime.datetime.now() - time)
#     y1.append(sum(hold)/1)
#     print(i)
# 
# 
# plt.title('Weights of MST for Dimension 0')
# plt.xlabel('Number of Vertices, n')
# plt.ylabel('Weight of MST')
# plt.plot(x1, y1)          
# =============================================================================
 
# dim = 2   
# =============================================================================
# x2 = []
# y2 = []
# 
# for i in test_numbers:
#     x2.append(i)
#     G = Graph2(i)
#     hold = []
#     for z in range(5):
#         random.seed(random.uniform(0,1000))
#         push = Prims(G, G.V[0])
#         hold.append(push)
#     y2.append(sum(hold)/5)
#     print(i)
#     print(datetime.datetime.now())
# 
# plt.title('Weights of MST for Dimension 2')
# plt.xlabel('Number of Vertices, n')
# plt.ylabel('Weight of MST')
# plt.plot(x2, y2)  
# =============================================================================

# dim = 3
# =============================================================================
# x3 = []
# y3 = []
# 
# for i in test_numbers:
#     x3.append(i)
#     G = Graph3(i)
#     hold = []
#     for z in range(5):
#         random.seed(random.uniform(0,1000))
#         push = Prims(G, G.V[0])
#         hold.append(push)
#     y3.append(sum(hold)/5)
#     print(i)
#     print(datetime.datetime.now())
# 
# plt.title('Weights of MST for Dimension 3')
# plt.xlabel('Number of Vertices, n')
# plt.ylabel('Weight of MST')
# plt.plot(x3, y3)  
# =============================================================================

# dim = 4
# =============================================================================
# x4 = []
# y4 = []
# 
# for i in test_numbers:
#     x4.append(i)
#     G = Graph4(i)
#     hold = []
#     for z in range(5):
#         random.seed(random.uniform(0,1000))
#         push = Prims(G, G.V[0])
#         hold.append(push)
#     y4.append(sum(hold)/5)
#     print(i)
#     print(datetime.datetime.now())
# 
# plt.title('Weights of MST for Dimension 3')
# plt.xlabel('Number of Vertices, n')
# plt.ylabel('Weight of MST')
# plt.plot(x4, y4)  
# =============================================================================


# parse arguments for running Python script from command line

parser = argparse.ArgumentParser(description='Python Script for Average MST Weight')
parser.add_argument('zero', help='flag', type=int, choices=[0])
parser.add_argument('numpoints', help='number of points', type=int)
parser.add_argument('numtrials', help='number of runs to be done', type=int)
parser.add_argument('dimension', help='dimension', type=int)
args = parser.parse_args()
if args.zero == 0:
    if args.dimension == 0:
        total = 0
        for i in range(args.numtrials):
            random.seed(random.uniform(0,1000))
            G = Graph1(args.numpoints)
            total += Prims(G, G.V[0])
        print(total/args.numtrials, args.numpoints, args.numtrials, args.dimension)
    elif args.dimension == 2:
        total = 0
        for i in range(args.numtrials):
            random.seed(random.uniform(0,1000))
            G = Graph2(args.numpoints)
            total += Prims(G, G.V[0])
        print(total/args.numtrials, args.numpoints, args.numtrials, args.dimension)
    elif args.dimension == 3:
        total = 0
        for i in range(args.numtrials):
            random.seed(random.uniform(0,1000))
            G = Graph3(args.numpoints)
            total += Prims(G, G.V[0])
        print(total/args.numtrials, args.numpoints, args.numtrials, args.dimension)
    elif args.dimension == 4:
        total = 0
        for i in range(args.numtrials):
            random.seed(random.uniform(0,1000))
            G = Graph4(args.numpoints)
            total += Prims(G, G.V[0])
        print(total/args.numtrials, args.numpoints, args.numtrials, args.dimension)
    else:
        print('wrong dimension, try again')       