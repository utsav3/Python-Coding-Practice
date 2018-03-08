# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:58:58 2018

@author: utsav
"""

def digit_square(num):
    digit_square=0
    final_number=0
    for d in range(0,num+1):
        digit_square= d*d
        final_number= final_number+digit_square
    return final_number

def sum_square(num):
    final_number=0
    for d in range(0,num+1):
        final_number=final_number+d
    return (final_number*final_number)

def main_fn(num):
    digit_sumsquare = digit_square(num)
    sum_numsquare = sum_square(num)
    print('The sum of the squares is: ',digit_sumsquare)
    print('The square of the sum: ',sum_numsquare)
    print('The difference is:', sum_numsquare-digit_sumsquare)
main_fn(10)