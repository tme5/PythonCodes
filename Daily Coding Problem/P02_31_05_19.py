#!python
'''
Daily Coding Problem

Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

Created on May 31, 2019

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

def get_prod(arr):
#    print(arr)
    prod=1
    for num in arr:
        prod=prod*num
    return prod

def prodArray(arr):
    if len(arr)<2:
        return arr
    temp_arr=arr.copy()
    ret_arr=[]
    for i in range(0,len(arr)):
        temp_arr.pop(i)
        prod=get_prod(temp_arr)
        ret_arr.insert(i,prod)
        temp_arr=arr.copy()
    return ret_arr

def prodArray1(arr):
    n=len(arr)
    temp=1
    prod=[1 for i in range(n)]
    
    for i in range(n):
        prod[i]=temp
        temp*=arr[i]
    
    temp=1
    
    for i in range(n-1,-1,-1):
        prod[i]*=temp
        temp*=arr[i]

    return prod    
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    new_arr1=prodArray1([1, 2, 3, 4, 5])
    print(new_arr1)    
    new_arr2=prodArray1([3, 2, 1])
    print(new_arr2)
        
if __name__ == '__main__': main()