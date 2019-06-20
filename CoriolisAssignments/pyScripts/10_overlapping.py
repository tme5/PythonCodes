#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

10) Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your overlapping() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
'''
def overlapping(lst1,lst2):
    '''Returns True if atleast one member in input lists is common, False otherwise.
    Time complexity of this function in worst condition is O(n)'''
    for obj in lst1:
        if obj in lst2:
            return True
    return False

if __name__=='__main__':
    print(overlapping(list('tushr'),list("radar")))
    #True
    print(overlapping(['1'],list("rad1dar")))
    #True
    print(overlapping([10,1,13,14],[1,2,3,4]))
    #True
    print(overlapping([10,11,13,14],[1,2,3,4]))
    #False
    
