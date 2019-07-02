'''
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

Created on 25-Jun-2019

@author: Lenovo
'''
def max_subarr(arr,k):
    ret_lst=[]
    i=0
    while i<=len(arr)-k:
        ret_lst.append(max(arr[i:i+k]))
        i+=1
    return ret_lst

def main():
    assert max_subarr([10,5,2,7,8,7],3)==[10,7,8,8], 'Wrong output'
    
if __name__=='__main__':
    main()