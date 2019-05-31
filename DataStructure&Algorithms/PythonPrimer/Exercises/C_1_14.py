'''
Created on Apr 2, 2019

@author: TME5
'''
def getOddProductPair(data):
    lst=[]
    for i in range(0,len(data)):
        num1=data[i]
        for j in range(0,len(data)):
            if i!=j:
                num2=data[j]
                if (num1*num2)%2 !=0:
                    if (num2,num1) not in lst:
                        lst.append((num1,num2))
    return lst

lst=[1,2,3,4,5,6,7,8]
print(getOddProductPair(lst))