#!python
'''
Created on May 29, 2019

@author: TME5
'''
# +---{ Import Section }---+
import time
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper
    
class Deque:
    def __init__(self):
        self.items=[]
    
    def add_front(self,item):
        self.items.insert(0,item)
    
    def add_rear(self,item):
        self.items.append(item)
    
    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items)==0
        
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    deque=Deque()
    print(deque.size())
    print(deque.is_empty())
    deque.remove_rear()
    deque.remove_front()
    
    deque.add_front('apple')
    print(deque.items)
    deque.add_front('banana')
    print(deque.items)
    deque.add_rear('cherry')
    print(deque.items)
    
    print(deque.size())
    print(deque.is_empty())
    
    deque.remove_front()
    print(deque.items)
    
    deque.remove_rear()
    print(deque.items)
    
    
if __name__ == '__main__': main()