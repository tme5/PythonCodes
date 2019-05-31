'''
Created on Apr 2, 2019

@author: TME5
'''
def reverseList(data):
    return data[::-1]
 
# def reverseList(data):
#     lst=[]
#     for i in range(len(data)-1,-1,-1):
#         lst.append(data[i])
#     return lst

lst=[0,1,2,3,7,8,9,9,10,12]
print(reverseList(lst))

lst.reverse()
print(lst)