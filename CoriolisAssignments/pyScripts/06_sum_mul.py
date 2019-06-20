#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

6) Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''

def sum(inp_list):
    '''Summation of all numbers in the input list'''
    if len(inp_list)==1:
        return inp_list[0]
    elif len(inp_list)>1:
        ret_sum=0
        for num in inp_list:
            if type(num)==int:
                ret_sum+=num
            else:
                raise Exception('Expected numeric list')
        return ret_sum
    else:
        raise Exception('Expected non empty list')

def multiply(inp_list):
    '''Multiplication of all numbers in the input list'''
    if len(inp_list)==1:
        return inp_list[0]
    elif len(inp_list)>1:
        ret_mul=1
        for num in inp_list:
            if type(num)==int:
                ret_mul*=num
            else:
                raise Exception('Expected numeric list')
        return ret_mul
    else:
        raise Exception('Expected non empty list')
    
if __name__=='__main__':
    print(sum([1, 2, 3, 4]))
    #10
    print(multiply([1, 2, 3, 4]))
    #24
    print(sum([10]))
    #10
    print(multiply([10]))
    #10
    #print(multiply([]))
    #Exception
    #print(multiply([1,'a']))
    #Exception
    