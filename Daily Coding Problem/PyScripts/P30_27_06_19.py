'''
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

Created on 28-Jun-2019

@author: Lenovo
'''
def get_trap_info(arr):
    trapped=0
    top=min(arr[0],arr[-1])
    i=1
    while i<len(arr)-1:
        prev=arr[i-1]
        next=arr[i+1]
        top_i=min(prev,next)
        if top_i>top and top_i>arr[i]:
            trapped+=top_i-arr[i]
        elif top>arr[i]:
            trapped+=top-arr[i]
        i+=1
    return trapped    
        
def main():
    assert get_trap_info([2,1,2])==1, 'Wrong trapped info'
    assert get_trap_info([3,0,1,3,0,5])==8, 'Wrong trapped info'
    assert get_trap_info([1,2,3,4,5])==0, 'Wrong trapped info'
    assert get_trap_info([1,2,3,1,4,1])==2, 'Wrong trapped info'

if __name__=='__main__':
    main()