#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM
15) Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
'''

def find_longest_word(lst):
    '''Returns a length of the longest string from the input list
    Time complexity of the function is O(n)'''
    ret_max=0
    for word in lst:
        if type(word)==str:
            if len(word)>ret_max:
                ret_max=len(word)
        else:
            raise Exception('Expected list of Strings')
    return ret_max


if __name__=='__main__':
    print(find_longest_word.__doc__)
    # Get the docstring of the function
    print(find_longest_word(['tushar','python','example','I','am']))
    #7
    
