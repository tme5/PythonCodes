#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM

31) Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.)
'''

def map1(func,it):
    '''Implementation of map using for loop
    Time complexity of this function in worst condition is O(n)'''
    ret=[]
    for i in it:
        ret.append(func(i))
    return ret

def map2(func,it):
    '''Implementation of map using comprehension
    Time complexity of this function in worst condition is O(1)'''
    return [func(x) for x in it]

def map3(func,it):
    '''Implementation of map using recursion'''
    ret=[]
    if it[1:]:
        ret.append(func(it[0]))
        ret.extend(map3(func,it[1:]))
    else:
        ret.append(func(it[0]))
    return ret
               
def filter1(func,it):
    '''Implementation of map using for loop
    Time complexity of this function in worst condition is O(n)'''
    ret=[]
    for i in it:
        if func(i):
            ret.append(i)
    return ret

def filter2(func,it):
    '''Implementation of map using comprehension
    Time complexity of this function in worst condition is O(1)'''
    return [x for x in it if func(x)]

def filter3(func,it):
    '''Implementation of map using recursion'''
    ret=[]
    if it[1:]:
        if func(it[0]):
            ret.append(it[0])
            ret.extend(filter3(func,it[1:]))
    else:
        if func(it[0]):
            ret.append(it[0])
    return ret

def reduce1(func,it):
    '''Implementation of map using while loop
    Time complexity of this function in worst condition is O(1)'''
    ret=it[0]
    i=1
    while i<len(it):
        ret=func(ret,it[i])
        i+=1
    return ret

def reduce2(func,it):
    '''Implementation of map using recursion
    Time complexity of this function in worst condition is O(1)'''
    ret=it[0]
    if it[1:]:
        ret=func(ret,reduce2(func,it[1:]))        
    else:
        ret=func(ret,it[0])
    return ret

if __name__=='__main__':
    print(map1(lambda x: x**2, [1,2,3,4,5,6]))
    #[1, 4, 9, 16, 25, 36]
    print(map2(lambda x: x**2, [1,2,3,4,5,6]))
    #[1, 4, 9, 16, 25, 36]
    print(map3(lambda x: x**2, [1,2,3,4,5,6]))
    #[1, 4, 9, 16, 25, 36]
    print(filter1(lambda x: len(x)>2,['tushar','python','example','I','am']))
    #['tushar', 'python', 'example']
    print(filter2(lambda x: len(x)>2,['tushar','python','example','I','am']))
    #['tushar', 'python', 'example']
    print(filter3(lambda x: len(x)>2,['tushar','python','example','I','am']))
    #['tushar', 'python', 'example']
    print(reduce1(lambda a,b:a if a>b else b,[1,2,3,4,45,1,3,34,5,6,8]))
    #45
    print(reduce2(lambda a,b:a if a>b else b,[1,2,3,4,45,1,3,34,5,6,8]))
    #45