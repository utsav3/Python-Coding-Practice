# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:24:11 2018

@author: utsav
"""

def square_num(num):
    digit_square=0
    final_number=0
    for d in str(num):
        #print(int(d))
        d = int(d)
        digit_square= d*d
        final_number= str(final_number)+str(digit_square)
        final_number=int(final_number)
    print(final_number)

square_num(2476)