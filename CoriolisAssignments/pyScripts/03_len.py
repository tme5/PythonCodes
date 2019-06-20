#!/usr/bin/python

'''
Date: 17-06-2019
Created By: TusharM

3) Define a function that computes the length of a given list or string. (It is true that pyScripts has the len() function built in, but writing it yourself is nevertheless a good exercise.)

'''

def len(inp):
    '''Get the length if string or list'''
    ret_val=0
    try:
        for elem in inp:
            ret_val+=1
        return ret_val
    except TypeError as error:
        print(error)

if __name__=='__main__':
    print(len.__doc__)
    # Get the docstring of the function
    print(len('tushar'))
    #6
    print(len(''))
    #0
    print(len([1,2,3,4,5]))
    #5
    print(len([]))
    #0
    print(len(1))
    #'int' object is not iterable