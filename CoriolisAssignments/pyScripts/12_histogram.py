#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

12) Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
'''
def histogram(lst):
    '''print Histogram using the input list
    Time complexity of this function in worst condition is O(1)'''
    for count in lst:
        print(count*'*')

if __name__=='__main__':
    histogram([4,9,7])
    print('---')
#     ****
#     *********
#     *******
    histogram([1,2,3,4,5])
#     *
#     **
#     ***
#     ****
#     *****
    print('---')
    histogram([5])
#     *****
    print('---')

    histogram([9,7,8,8,5,2,3])
#     *********
#     *******
#     ********
#     ********
#     *****
#     **
#     ***
    print('---')
