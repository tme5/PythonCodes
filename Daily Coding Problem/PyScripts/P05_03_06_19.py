'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

Created on Jun 3, 2019

@author: Administrator
'''
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(cons):
    return cons(lambda a,b: a)

def cdr(cons):
    return cons(lambda a,b: b)

p1=cons('apple','banana')
print(car(p1))
print(cdr(p1))


