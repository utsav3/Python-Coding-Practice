# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:09:34 2018

@author: utsav
"""

def char_split(direction):
    char_list = []
    char_list = list(direction)
    return char_list

def char_count(direction):
    direction_list = []
    direction_list=char_split(direction)
    length=len(direction_list)
    if length==10:
        return True
    return False

def check_even(direction):
    direction_list = []
    direction_list = char_split(direction)
    w_count=direction_list.count('W')
    e_count=direction_list.count('E')
    n_count=direction_list.count('N')
    s_count=direction_list.count('S')
    if w_count == e_count:
        if s_count == n_count:
            print('TRUE')
        else:
            print('FALSE')
    else:
        print('FALSE')


def main_fn(direction):
   if not char_count(direction):
       print('FALSE')
   else:
       check_even(direction)

main_fn('WWEENNSSNS')

