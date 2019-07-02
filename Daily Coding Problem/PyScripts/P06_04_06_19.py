'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

Created on Jun 3, 2019

@author: Administrator
'''
class Node:
    def __init__(self,data,prev,nxt):
        self.val=data
        self.npx=prev ^ nxt
    
    def nextNodeIndex(self,prev):
        return self.npx ^ prev
    
    def prevNodeIndex(self,nxt):
        return self.npx ^ nxt
    
class XOR_DLL:
    def __init__(self,data,prev,nxt):
        self.mem=[Node(data,prev,nxt)]
        
    def head(self):
        return -1,0,self.mem[0]
    
    def add(self,data):
        prev_ind,cur_ind,cur_node=self.head()
        while True:
            next_ind=cur_node.nextNodeIndex(prev_ind)
            if next_ind==-1:
                break
            prev_ind,cur_ind=cur_ind,next_ind
            cur_node=self.mem[next_ind]
        self.mem.append(Node(data,cur_ind,-1))
        
    def get(self,ind):
        if ind==0:
            return self.mem[0]
        elif ind>=len(self.mem):
            return None
        else:
            return self.mem[ind]
    
def main():
    xor_dll_1=XOR_DLL(0,-1,0)
    for x in range(1,10):
        xor_dll_1.add(x)   
    assert xor_dll_1.get(5).val==5, 'Wrong Node value'
    
if __name__=='__main__':
    main()
        
            
            
    
        