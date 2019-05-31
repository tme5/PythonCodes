#!python
'''
Created on Apr 1, 2019

@author: TME5
'''
# Standard Generators
def TopTen():
    for i in range(1,11):
        yield i*i
        
        
values=TopTen()
for i in values:
    print(i,end=', ')
    
# Fibonacci Generator
print('\n----------------------')
def fibonacci(num):
    a=0
    b=1
    for i in range(num):
        yield b
        nxt=a+b
        a=b
        b=nxt
        
fib1=fibonacci(10)
for i in fib1:
    print(i,end=', ')