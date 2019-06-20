#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM
28) Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
'''
from functools import reduce

def find_longest_word(lst):
    '''Returns a length of the longest string from the input list
    Time complexity of the function is O(1)'''
    return reduce(lambda a,b:a if a>b else b,[len(x) for x in lst]) 

if __name__=='__main__':
    print(find_longest_word.__doc__)
    # Get the docstring of the function
    print(find_longest_word(['tushar','python','example','I','am']))
    #7
    
