#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

8) Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
'''

def is_palindrome(inp):
    '''Check if input string in palindrome or not, Return True if palindrome else False
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        temp=list(inp)
        while len(temp)>1:
            if temp.pop().lower() != temp.pop(0).lower():
                return False
        return True
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(is_palindrome("radar"))
    #True
    print(is_palindrome("raddar"))
    #True
    print(is_palindrome("testing"))
    #False
    
