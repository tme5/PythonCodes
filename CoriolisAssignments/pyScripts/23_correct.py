#!/usr/bin/python
'''
Date: 18-06-2019
Created By: TusharM

23) Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!
'''
import re

def correct(inp):
    '''Corrects the input string with 1) two or more occurences of the space character is compressed into one 2) extra space after a period if missing.
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        temp=re.sub(r' +',' ',inp)
        temp=re.sub(r'\.(?! )','. ',temp)
        return ''.join(temp)
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(correct("This   is  very funny  and    cool.Indeed!"))
    #This is very funny and cool. Indeed!
    print(correct("This   is  very funny  and    cool. Indeed!"))
    #This is very funny and cool. Indeed!