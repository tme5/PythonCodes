'''
Created on Apr 2, 2019

@author: TME5
'''
import random
def shuffle_1(data):
    for i in range(len(data)-2,0,-1):
        j=random.randint(1,i+1)
        print(i,j)
        data[i],data[j]=data[j],data[i]
    return data

lst=[1,2,3,4,5,6,7,8,9,10]
print(shuffle_1(lst))
