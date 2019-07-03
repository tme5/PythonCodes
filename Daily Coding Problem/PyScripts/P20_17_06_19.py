'''
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

Created on 25-Jun-2019

@author: Lenovo
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_at_end(self,data):
        new_node=Node(data)
        curr_node=self.head
        if curr_node==None:
            self.head=new_node
        else:
            while curr_node.next!=None:
                curr_node=curr_node.next
            curr_node.next=new_node
                           
    def get_node(self,in_data):
        curr_node=self.head
        if curr_node.data==in_data:
            return curr_node
        while curr_node.next!=None:
            if curr_node.data==in_data:
                return curr_node
            curr_node=curr_node.next       
        
    def get_list(self):
        curr_node=self.head
        ret_val=[]
        if curr_node==None:
            return 
        else:
            ret_val.append(curr_node.data)
            while curr_node.next!=None:
                curr_node=curr_node.next
                ret_val.append(curr_node.data)
        return ret_val

def get_intersection(l_l1,l_l2):
    l1_list=l_l1.get_list()
    l2_list=l_l2.get_list()
    for val in l1_list:
        if val in l2_list:
            return l_l2.get_node(val)
    
if __name__ == '__main__':    
    sll1=LinkedList()
    sll1.insert_at_end(3)
    sll1.insert_at_end(7)
    sll1.insert_at_end(8)
    sll1.insert_at_end(10)
    
    sll2=LinkedList()
    sll2.insert_at_end(99)
    sll2.insert_at_end(1)
    sll2.insert_at_end(15)
    sll2.insert_at_end(8)
    sll2.insert_at_end(10)
    
    intx_node=get_intersection(sll1, sll2)
    assert intx_node.data==8, 'Wrong output'
    #8