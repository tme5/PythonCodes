#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

7) Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
'''

def reverse(inp):
    '''Reverses the input string'''
    if type(inp)==str:
        return ''.join(inp[::-1])
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(reverse("I am testing"))
    #gnitset ma I
    print(reverse('this is fun'))
    #nuf si siht
    print(reverse('this, is fun.!#'))
    ##!.nuf si ,sihton
    
