'''
Created on Apr 2, 2019

@author: TME5
'''
lst=[1,2,3,4,5]
try:
    lst[5]=6
except Exception as e:
    print('Don\'t try buffer overflow attacks in Python!')
    