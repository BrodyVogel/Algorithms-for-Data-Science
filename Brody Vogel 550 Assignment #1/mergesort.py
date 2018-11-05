#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:18:17 2018

@author: vogebr01
"""

# Implements Merge Sort. If running in shell, use main() [stdin];
# if running in IDE, use main1() [input()].

import sys

def Merge(a, b):   
    list1 = list(a)
    list2 = list(b)
    
    if list1 == []:
        return(list2)
        
    elif list2 == []:
        return(list1)
        
    elif list1[0] <= list2[0]:
        u = list1.pop(0)
        
    else:
        u = list2.pop(0)
    
    return([u] + Merge(list1, list2))

def MergeSort(aList):
    finalList = []
    
    for x in aList:
        finalList.append([x])
    
    if len(aList) == 0:
        return("That's an empty list")
    
    elif len(aList) == 1:
        return(aList)
        
    else:
        
        while len(finalList) >= 2:
            u = finalList.pop(0)
            v = finalList.pop(0)
        
            finalList.append(Merge(u, v))
    
        return(finalList[0])

# For shell
def main():

    print("Enter the list to be sorted: ")

    srt = sys.stdin.readline()
    
    srt = list(map(int, srt.split(",")))
    
    print(MergeSort(srt))     
    
# For IDE
def main1():
    
    srt = input("Enter the list to be sorted: ")
    
    srt = list(map(int, srt.split(",")))
    
    print(MergeSort(srt))
    
#main()
main1()
    