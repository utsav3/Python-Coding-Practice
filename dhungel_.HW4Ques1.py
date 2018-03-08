# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:06:06 2018

@author: utsav
"""

def create():
    """
        Creates a test file and writes into it
    """
    f = open("test.txt", 'w+')
    for x in range(0,3):
        f.write("This is Line {} \n".format(x+1))
        if x==1:
            v=f.seek(0,1)
    f.seek(0,0)
    lines = f.readlines()
    lines=[line.rstrip() for line in lines]
    print(lines[0],lines[1],sep="\n")
    f.write("This is the fourth line \n")
    f.seek(v,0)  
    print(f.read())
    f.close()
create()