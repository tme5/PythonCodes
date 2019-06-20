#!/usr/bin/python

'''
Date: 17-06-2019
Created By: TusharM
1) Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in pyScripts. (It is true that pyScripts has the max() function built in, but writing it yourself is nevertheless a good exercise.)
'''

def max(num1,num2):
    '''Get the maximum of input1 and input2'''
    if type(num1)==int and type(num2)==int:
        if num1>num2:
            return num1
        return num2
    else:
        raise Exception('Invalid input, expected numbers')

if __name__=='__main__':
    print(max.__doc__)
    # Get the docstring of the function
    print(max(5,10))
    # 10
    #print(max('5',10))
    # Exception
    print(max(-5,-10))
    #-5
    print(max(-5,0))
    #0
