'''
Created on Apr 4, 2019

@author: TME5
'''
import time
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        diff=t2-t1
        print(f'Elapsed time: {diff} s')
    return wrapper


def factors(n):
    k=1
    last=[]
    while k*k <= n:
        if n%k==0:
            yield k
            if k!=(n//k):
                last.append(n//k)
        k+=1
    last.sort()
    for num in last:
        yield num

@elapsed_time
def main():        
    for num in factors(100):
        print(num,end=',')
        
if __name__ == '__main__': main()