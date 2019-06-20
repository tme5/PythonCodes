#!/usr/bin/python

'''
Date: 17-06-2019
Created By: TusharM

2) Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''

def max_of_three(num1,num2,num3):
    '''Get the maximum of 3 numbers'''
    if type(num1)==int and type(num2)==int and type(num3)==int:
        if num1>num2:
            if num1>num3:
                return num1
            else:
                return num3
        elif num2>num3:
            return num2
        return num3
    else:
        raise Exception('Invalid input, expected numbers')

if __name__=='__main__':
    print(max_of_three.__doc__)
    # Get the docstring of the function
    print(max_of_three(15,15,15))
    #15
    print(max_of_three(5,10,15))
    # 10
    #print(max('5',10,15))
    # Exception
    print(max_of_three(0,-5,-10))
    #-5
    print(max_of_three(-5,5,0))
    #0
    