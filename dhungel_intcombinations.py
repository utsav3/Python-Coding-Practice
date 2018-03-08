# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:45:50 2018

@author: utsav
"""
import math

def remove_duplicate(my_list=[]):
    newList = []
    for i in my_list:
        if i not in newList:
            newList.append(i)
    newList.sort()
    return newList

def integer_combination(h_range=[], t_range=[]):
    final_list = []
    for h in range(h_range[0],h_range[1]+1):
        for t in range(t_range[0],t_range[1]+1):
           final_list.append(int(math.pow(h,t))) 
    final_list=remove_duplicate(final_list)
    print (len(final_list))

x=5
y=5
integer_combination([2,x],[2,y])