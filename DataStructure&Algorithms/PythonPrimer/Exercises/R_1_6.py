'''
Created on Apr 2, 2019

@author: TME5
'''
def sqSumOdd(n):
    return sum(x*x for x in range(1,n) if x%2!=0)

print(sqSumOdd(2))
print(sqSumOdd(3))
print(sqSumOdd(10))