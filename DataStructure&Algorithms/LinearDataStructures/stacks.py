#!python
'''
Created on May 28, 2019

@author: TME5
'''
# +---{ Import Section }---+
import sys,os,time
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        '''Accepts an item as a parameter and appends to the end of the list
        Returns Nothing
        
        The runtime for this method is O(1), or constant time, because appending to the end of a
        list happens in constant time.
        '''
        self.items.append(item)
    
    def pop(self):
        '''Remove and returns the last item from the list, which is also the top item of the Stack.
        
        The run time here is constant time, because all it does is index to the last item of the list.        
        '''
        if self.items:
            return self.items.pop()
        return None
    
    def peek(self):
        '''Returns the last item in the list, which is also the item at the top of the Stack.
        
        The run time here is constant time, because indexing is done in constant time.        
        '''
        if self.items:
            return self.items[-1]
        return None
    
    def size(self):
        '''Returns the length of the list that is representing the Stack.
        The runtime here is constant time, because find length of list also happens in constant time.
        '''
        return len(self.items)
    
    def is_empty(self):
        '''Returns a Boolean value describing if the Stack is empty or not.
        Testing of equality happens in constant time.
        ''' 
        return self.items==[]
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    my_stack=Stack()
    print(my_stack.is_empty())
    print(my_stack.size())
    my_stack.pop()
    my_stack.peek()
    my_stack.push('apple')
    print(my_stack.is_empty())
    print(my_stack.items)
    my_stack.push('banana')
    print(my_stack.size())
    print(my_stack.peek())
    print(my_stack.items)
    my_stack.pop()
    print(my_stack.items)
    
if __name__ == '__main__': main()