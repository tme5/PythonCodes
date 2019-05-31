#!python
'''
Created on May 28, 2019

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
    
class Queue:
    def __init__(self):
        self.items=[]
        
    def enqueue(self,item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items==[]
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    my_queue=Queue()
    print(my_queue.is_empty())
    my_queue.dequeue()
    my_queue.enqueue('apple')
    my_queue.enqueue('banana')
    print(my_queue.peek())
    print(my_queue.size())
    print(my_queue.items)
    my_queue.dequeue()
    print(my_queue.peek())
    print(my_queue.items)
    
    
    
    
if __name__ == '__main__': main()