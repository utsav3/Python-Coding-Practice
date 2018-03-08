# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:07:40 2018

@author: utsav
"""

def book(person_names):
   length = len(person_names)
   if length==0:
       print('no one has read this')
   elif length ==1:
       print(person_names[0], 'has read this')
   elif length ==2:
       print(person_names[0],'and',person_names[1], 'have read this')
   elif length==3:
       
       print('{}, {} and {}'.format(person_names[0],person_names[1],person_names[2]), 'have read this')
   elif length >=4:
       print('{}, {}'.format(person_names[0],person_names[1]), 'and',length-2 ,'others have read this')
   
#INPUT FUNCTION   
book(['Hari','Ram','Sam','Raj','Ram'])