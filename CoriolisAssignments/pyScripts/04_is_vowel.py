#!/usr/bin/python

'''
Date: 17-06-2019
Created By: TusharM

4) Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

'''

def is_vowel(inp):
    '''Check if the input character is vowel Returns True if vowel else False'''
    vowels=['a','e','i','o','u']
    if type(inp)==str and len(inp)==1:
        if inp.lower() in vowels:
            return True
        return False
    else:
        raise Exception('Input must be string of length 1')

if __name__=='__main__':
    print(is_vowel.__doc__)
    # Get the docstring of the function
    print(is_vowel('T'))
    #False
    print(is_vowel('A'))
    #True
    print(is_vowel('t'))
    #False
    print(is_vowel('a'))
    #True
    #print(is_vowel('tushar'))
    #Exception
    #print(is_vowel(1))
    #Exception