#!python
'''
Created on Apr 4, 2019

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
    
def norm(v,p):
    summation=0
    for num in v:
        summation=summation+num**p
    return summation**(1/p)
     
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    print(norm([4,3],2))
if __name__ == '__main__': main()