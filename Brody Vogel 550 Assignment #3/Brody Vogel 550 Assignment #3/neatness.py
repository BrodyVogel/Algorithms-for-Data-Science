#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:10:56 2018

@author: vogebr01
"""

import math

def neatness(M):
    # read the text of the review into a list of words
    text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. The three-disc collection includes all 12 episodes as well as many extras. There is a collection of interviews by the show's creator Joss Whedon in which he explains his inspiration for the show as well as comments on the various cast members.  Much of the same material is covered in more depth with Whedon's commentary track for the show's first two episodes that make up the Buffy the Vampire Slayer pilot. The most interesting points of Whedon's commentary come from his explanation of the learning curve he encountered shifting from blockbuster films like Toy Story to a much lower-budget television series. The first disc also includes a short interview with David Boreanaz who plays the role of Angel. Other features include the script for the pilot episodes, a trailer, a large photo gallery of publicity shots and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, Alyson Hannigan and Nicholas Brendon."
    t = text.split(" ")
    
    # n parameter
    n = len(t)
    
    # build the penalty matrix
    # had to make changes for Python's 0-indexing
    penalty = [[math.inf]*n for x in range(n)]
    cost = [math.inf]*(n+1)
    cost[0] = 0
    place = [math.inf]*n
    for i in range(0,n):
        for j in range(i,n):
            if M - j + i - sum([len(z) for z in t[i:j+1]]) < 0:
                penalty[i][j] = math.inf
            else:
                if j == n-1 and M - j + i - sum([len(z) for z in t[i:]]) >= 0:
                    penalty[i][j] = 0
                else:
                    penalty[i][j] = (M - j + i - sum([len(z) for z in t[i:j+1]]))**3
    
    # build the cost and place arrays 
    # same indexing changes
    for x in range(n):
        for y in range(x+1):
            if cost[y] + penalty[y][x] < cost[x+1]:
                cost[x+1] = penalty[y][x] + cost[y]
                place[x] = y
                
    # get the minimal total cost
    total = cost[-1]

    lines = []
    
    # print the text "pretty" by walking backwards through place
    a = n
    b = 0
    while a >= b:
        lines.append(t[place[a-1]:a])
        a = place[a-1]
        b = place[a-1]
        
    lines = lines[::-1]
    
    print('\n')
    
    for line in lines:
        print(' '.join(word for word in line))

    print('\n')
    print("Minimum Penalty with M = ", M, ": ", total)	

def main():
    neatness(40)
    neatness(72)
    
main()
