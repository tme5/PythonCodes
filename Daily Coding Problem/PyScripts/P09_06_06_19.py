'''
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?

Created on 25-Jun-2019

@author: Lenovo
'''
def max_non_adj_sum1(arr):
    incl = 0
    excl = 0
    for i in arr: 
        incl,excl=excl+i, excl if excl>incl else incl 
    return (excl if excl>incl else incl) 

def max_non_adj_sum(arr):
    #incl=max(old incl , excl+ curr)
    #excl=old incl
    incl = arr[0]
    excl = 0
    for i in arr[1:]:
        incl,excl=max(incl,excl+i),incl 
    return (excl if excl>incl else incl)        

def main():
    print(max_non_adj_sum([2,4,6,2,5]))
    print(max_non_adj_sum([5,1,1,5]))
    print(max_non_adj_sum([5,5,10,100,10,5]))
    print(max_non_adj_sum([1,2,3]))
    print(max_non_adj_sum([1,20,3]))
    
if __name__=='__main__':
    main()