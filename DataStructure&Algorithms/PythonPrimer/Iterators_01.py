#!python
'''
Created on Apr 1, 2019

@author: TME5
'''
# Standard Iterators
lst=[7,9,5,2,10]
for i in lst:
    print(i)
    
it=iter(lst)
print(it.__next__())
print(next(it))

# Custom Iterators 
print('--------- Custom Iterators ---------')
class TopTen:
    def __init__(self):
        self.num=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=TopTen()
print(values.__next__())
print('----')
print(next(values))
print('----')
for i in values:
    print(i)