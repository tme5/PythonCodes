#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM
14) Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
'''

def map_len_list(lst):
    '''Returns a list of length of words corresponding to the input list
    time complexity of the function is O(n)'''
    ret_list=[]
    for word in lst:
        if type(word)==str:
            ret_list.append(len(word))
        else:
            raise Exception('Expected list of Strings')
    return ret_list


if __name__=='__main__':
    print(map_len_list.__doc__)
    # Get the docstring of the function
    print(map_len_list(['tushar','python','example','I','am']))
    #[6, 6, 7, 1, 2]
    
