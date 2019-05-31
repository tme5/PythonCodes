#!python
'''
Created on May 28, 2019

@author: TME5
'''
# +---{ Import Section }---+

from LinearDataStructures.queues import *
import random
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

class Job:
    def __init__(self):
        self.pages=random.randint(1,11)
    
    def print_page(self):
        if self.pages >0:
            self.pages-=1
            
    def check_complete(self):
        if self.pages==0:
            return True
        return False

class PrintQueue(Queue):
    def __init__(self):
        self.items=[]
    
class Printer():
    def __init__(self):
        self.current_job=None
    
    def get_job(self,print_queue):
        try:
            self.current_job=print_queue.dequeue()
        except IndexError:
            return "No more jobs to Print."
    
    def print_job(self,job):
        while job.pages>0:
            job.print_page()
        
        if job.check_complete():
            return "Printing complete."
        else:
            return "An error occurred."     

# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    job1=Job()
    print(job1.pages)
    job2=Job()
    print(job2.pages)
    print_q=PrintQueue()
    printer=Printer()
    print_q.enqueue(job1)
    print_q.enqueue(job2)
    print(print_q.items)
    printer.get_job(print_q)
    print(print_q.items)
    print(printer.print_job(printer.current_job))
    printer.get_job(print_q)
    print(print_q.items)
    print(printer.print_job(printer.current_job))
    
if __name__ == '__main__': main()