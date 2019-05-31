#!python
'''
Created on Apr 2, 2019

@author: TME5
'''
def is_multiple(n,m):
    if n%m==0:
        return True
    else:
        return False

print(is_multiple(10, 5))
print(is_multiple(7, 3))