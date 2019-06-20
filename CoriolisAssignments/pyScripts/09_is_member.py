#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

9) Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend pyScripts did not have this operator.)
'''
def is_member(elem,lst):
    '''Check if element is present in the input list
    Time complexity of this function in worst condition is O(n)'''
    for obj in lst:
        if type(str)==type(elem):
            if elem == obj:
                return True
        else:
            if str(elem) == str(obj):
                return True
    return False

if __name__=='__main__':
    print(is_member('r',list("radar")))
    #True
    print(is_member(1,list("rad1dar")))
    #True
    print(is_member(1,list("radar")))
    #False
    print(is_member(1,[1,2,3,4]))
    #True
    
