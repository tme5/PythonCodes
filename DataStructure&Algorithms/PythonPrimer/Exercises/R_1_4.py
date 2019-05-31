#!python
'''
Created on Apr 2, 2019

@author: TME5
'''
def sqSum(n):
    return sum(x*x for x in range(1,n))

print(sqSum(2))
print(sqSum(3))
print(sqSum(10))