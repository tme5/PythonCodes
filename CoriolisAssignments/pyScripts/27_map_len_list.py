#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM
27) Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
'''

def map_len_list_1(lst):
    '''Returns a list of length of words corresponding to the input list
    time complexity of the function is O(n)'''
    ret_list=[]
    for word in lst:
        if type(word)==str:
            ret_list.append(len(word))
        else:
            raise Exception('Expected list of Strings')
    return ret_list

def map_len_list_2(lst):
    '''Returns a list of length of words corresponding to the input list
    time complexity of the function is O(1)'''
    return list(map(lambda x: len(x),lst))

def map_len_list_3(lst):
    '''Returns a list of length of words corresponding to the input list
    time complexity of the function is O(1)'''
    return [len(x) for x in lst]

if __name__=='__main__':
    print(map_len_list_1(['tushar','python','example','I','am']))
    #[6, 6, 7, 1, 2]
    print(map_len_list_2(['tushar','python','example','I','am']))
    #[6, 6, 7, 1, 2]
    print(map_len_list_3(['tushar','python','example','I','am']))
    #[6, 6, 7, 1, 2]
