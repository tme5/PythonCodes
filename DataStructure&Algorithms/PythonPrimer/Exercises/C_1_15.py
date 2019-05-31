'''
Created on Apr 2, 2019

@author: TME5
'''
def checkUnq(data):
    if len(set(data))==len(data):
        return True
    else:
        return False

lst=[1,2,3,4,5,6,7,8,8,8,7,655,4,3]
print(checkUnq(lst))

lst=[1,2,3,4,5,6]
print(checkUnq(lst))