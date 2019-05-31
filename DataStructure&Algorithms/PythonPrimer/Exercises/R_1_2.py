#!python
'''
Created on Apr 2, 2019

@author: TME5
'''
# def is_even(k):
#     if k%2==0:
#         return True
#     else:
#         return False

# def is_even(k):
#     if k&1==1:
#         return False
#     else:
#         return True

def is_even(k):
    isEven=True
    for i in range(1,k+1):
        if isEven==True:
            isEven=False
        else:
            isEven=True 
    return isEven
  
print(is_even(5))
print(is_even(6))