#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM
26) Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
'''

from functools import reduce
def max_in_list(lst):
    '''Get the maximum from input list 
    Time complexity of the function is O(1)'''
    return reduce(lambda a,b:a if a>b else b,lst)

if __name__=='__main__':
    print(max_in_list.__doc__)
    # Get the docstring of the function
    print(max_in_list([1,2,3,4,45,1,3,34,5,6,8]))
    #45
