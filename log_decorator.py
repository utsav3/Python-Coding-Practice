# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:23:46 2018

@author: utsav dhungel
"""

import sys
import string
import copy
import time
import logging

def log(file_name=None):
    FORMAT = '%(message)s '
                
    def decorator_f(f):
        
        def wrap_f(*args):
            if file_name is not None:
                try:
                    fp = open (file_name,'a')
                    sys.stdout = fp
                except ValueError:
                    pass
            
            logger = logging.getLogger("log_decorator")
            logger.setLevel(logging.DEBUG)
            st_handler = logging.StreamHandler(sys.stdout)
            st_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter(FORMAT)
            st_handler.setFormatter(formatter)
            logger.addHandler(st_handler)
            logger.info("*******************************************************************")
            logger.info("Calling Function "+  f.__name__)
            
            if args is not None:
                logger.info("Arguments: ")
                for arg in args:
                    logger.info(''+ str(arg)
                                      + ' of type ' 
                                      + type(arg).__name__)
            else:
                logger.info("No Arguments")
            logger.info('Output: ')
            start_time=time.time()    
            retval = f(*args)
            end_time = time.time()
            
            logger.info("Time of execution: {:f} s.".format((end_time-start_time)))
            if retval is None:
                logger.info('No return value')
            else:
                logger.info('Return value: '
                             + str(retval)
                             + ' of type '
                             + type(retval).__name__)
            logger.info("*******************************************************************")
            x = logger.handlers.copy()
            for i in x:
                logger.removeHandler(i)
                i.flush()
                i.close()
          
        return wrap_f        
    return decorator_f

        

def main():
   factorial(7)
   square_sum(3,4)
    
@log("logger4.log")
def factorial(number):
    time.sleep(1)
    res =int(number)
    for i in range(1,number):
        res = i*res
    print(res)
    return res
    
@log("logger4.log")
def square_sum(number1, number2):
    time.sleep(1)
    print(number1*number2)
    return number1*number2
    


if __name__ == "__main__":
    main()