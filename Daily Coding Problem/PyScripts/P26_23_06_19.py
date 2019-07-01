'''
This problem was asked by Google.
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.

Created on 25-Jun-2019

@author: Lenovo
'''
class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class Singly_Linked_List:
    def __init__(self):
        self.head=None
    
    def length(self):
        if not self.head:
            return 0
        count=1
        cur_node=self.head
        while cur_node.next:
            count+=1
            cur_node=cur_node.next
        return count 
    
    def insert_before(self,data):
        node=Node(data)
        if self.head:
            node.next=self.head
        self.head=node
    
    def insert_after(self,data):
        node=Node(data)
        if self.head:
            cur_node=self.head
            while cur_node.next:
                cur_node=cur_node.next
            cur_node.next=node
        else:
            self.head=node
    
    def print_SLL(self):
        if self.head:
            cur_node=self.head
            print(cur_node.value,end=' ')
            while cur_node.next:
                cur_node=cur_node.next
                print(cur_node.value,end=' ')
        print('\n')
    
    def delete_at(self,k):
        if k>self.length()-1:
            return
        cur_node=self.head
        if k==0:
            self.head=cur_node.next
            del cur_node
        else:
            i=1
            prev_node=self.head
            cur_node=prev_node.next
            while cur_node.next:
                if i==k:
                    prev_node.next=cur_node.next
                    del cur_node
                    return
                i+=1
                prev_node=cur_node
                cur_node=cur_node.next
                
def main():
    sll_1=Singly_Linked_List()
    for i in range(10):
        sll_1.insert_after(i)
    sll_1.print_SLL()
    sll_1.delete_at(5)
    sll_1.print_SLL()
    sll_1.delete_at(0)
    sll_1.print_SLL()
    assert sll_1.delete_at(8)==None,'Shouldn\'t delete'
    
if __name__=='__main__':
    main()
        