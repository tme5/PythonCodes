#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM
13) The function max_in_list() from exercise 1) and the function max_in_list_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list_in_list() that takes a list of numbers and returns the largest one.
'''

def max_in_list(lst):
    '''Get the maximum from input list 
    Time complexity of the function is O(n)'''
    temp=lst.copy()
    temp.sort()
    return temp[-1]

def max_in_list_1(lst):
    '''Get the maximum from input list 
    Time complexity of the function is O(n)'''
    ret_max=lst[0]
    for num in lst:
        if ret_max < num:
            ret_max=num
    return ret_max

if __name__=='__main__':
    print(max_in_list.__doc__)
    # Get the docstring of the function
    print(max_in_list_1([1,2,3,4,45,1,3,34,5,6,8]))
    #45
