# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:41:20 2018

@author: utsav
"""
def toChars(num):
    rev_list = []
    while num > 0:
        rev_list.append(num%10)
        num = int(num/10)
    return list(reversed(rev_list))

def encript_message(message,key):
    lis= list(message)
    key_list = toChars(key)
    
    list_num = list((ord(x)-96 for x in lis))
    encrypted_msg = []
    y=0    
    for x in range(0,len(list_num)):
        encrypted_msg.append(list_num[x]+key_list[y])
        y= y+1
        if y==len(key_list):
            y=0
        
    print(list_num)
    print(encrypted_msg)

#INPUT DUNCTION
encript_message('applepie',1824)

