'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

Created on Jun 3, 2019
@author: Administrator
'''
def find_missing(arr):
    arr=[x for x in arr if x>=0]
    arr.sort()
    i=0
    while True:
        if i==len(arr)-1:
            return arr[-1]+1
        else:
            temp=arr[i+1]
            prev=arr[i]
            if temp>0:
                if temp!=prev+1:
                    return prev+1
        i+=1
            

def main():
    assert find_missing([3,4,-1,1])==2, 'Wrong missing positive integer'
    assert find_missing([1,2,0])==3, 'Wrong missing positive integer'
    
if __name__=='__main__':
    main()