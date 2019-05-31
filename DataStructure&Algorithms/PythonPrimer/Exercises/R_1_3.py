#!python
'''
Created on Apr 2, 2019

@author: TME5
'''
def minmax(data):
    mini=data[0]
    maxi=data[0]
    if len(data)>1:
        for i in range(1,len(data)):
            if data[i]>maxi:
                maxi=data[i]
            if data[i]<mini:
                mini=data[i]
    return (mini,maxi)

lst=[10,1,3,5,67,8]
print(minmax(lst))

lst=[1]
print(minmax(lst))

lst=[1,10]
print(minmax(lst))
        
lst=[1,1]
print(minmax(lst))