#!python
'''
Created on May 29, 2019

@author: TME5
'''
# +---{ Import Section }---+
from LinearDataStructures.deques import *
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

def is_palindrome(word):
    my_d=Deque()
    for char in word:
        my_d.add_front(char)
        
    while my_d.size()>=2:
        front_char=my_d.remove_front()
        rear_char=my_d.remove_rear()
        if front_char != rear_char:
            return False
    return True
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    Words=['mom','kayak','non','moon','racecar']
    for word in Words:
        if is_palindrome(word):
            print(f'{word} is palindrome.')
        else:
            print(f'{word} is not palindrome.')
    
if __name__ == '__main__': main()