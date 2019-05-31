#!python
'''
Daily Coding Problem
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

Created on May 30, 2019

@author: TME5
'''
# +---{ Import Section }---+
import time
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper
    
def isPartitionsInlist(int_list,k):
    temp_list=int_list.copy()
    for i in range(0,len(temp_list)):
        p1=temp_list.pop(i)
        if k-p1 in temp_list:
            return True
        temp_list=int_list.copy()
    return False
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    print(isPartitionsInlist([10,15,3,7], 17))
    #True
    print(isPartitionsInlist([10,15,3,7], 20))
    #False
    
if __name__ == '__main__': main()