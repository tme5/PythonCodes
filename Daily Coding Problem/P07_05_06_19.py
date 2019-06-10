#!python
'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

Created on Jun 5, 2019

@author: Administrator
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
           
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    pass
        
            
if __name__ == '__main__': main()
