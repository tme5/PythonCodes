'''
This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

Created on 25-Jun-2019

@author: Lenovo
'''
import time
from threading import Thread

def delay(f,ms):
    time.sleep(ms)
    f()

def func(name):
    print(f'Hello {name}')
    
job=Thread(target=delay,args=(lambda : func('Tushar'),1))
job.start()
