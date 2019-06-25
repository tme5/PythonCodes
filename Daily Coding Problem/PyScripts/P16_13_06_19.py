'''

 Daily Coding Problem
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

Created on 25-Jun-2019

@author: Lenovo
'''

class log:
    def __init__(self):
        self.data=[]
    
    def record(self,order_id):
        self.data.append(order_id)
    
    def get_last(self,num):
        if num==0 or num==None:
            raise Exception('expected number to be greater than 0')
        elif num<=len(self.data):
            i,ret_val=0,[]
            while i<num:
                ret_val.append(self.data[len(self.data)-1-i])
                i+=1
            return ret_val[::-1]            
        else:
            raise Exception('expected number to be less than length of records')
        
my_log=log()
my_log.record(1011)
my_log.record(1012)
my_log.record(1013)
my_log.record(1014)
my_log.record(1015)

print(my_log.get_last(3))
print(my_log.get_last(5))
#print(my_log.get_last(0))
#print(my_log.get_last(6))
        