#!python
'''
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 
Created on Jun 5, 2019

@author: Administrator
 '''

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def left(self,data):
        self.left=data
    
    def right(self,data):
        self.right=data
#     def insert(self,data):
#         if self.data:
#             if data<self.data:
#                 if self.left==None:
#                     self.left=Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data>self.data:
#                 if self.right==None:
#                     self.right=Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data=data
            
    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

def is_unival(root):
    if root==None:
        return True
    if root.left!=None and root.left.data!=root.data:
        return False
    if root.right!=None and root.right.data!=root.data:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    return False

def count_univals(root):
    if root==None:
        return 0
    total_count=count_univals(root.left)+count_univals(root.right)
    if is_unival(root):
        total_count+=1
    return total_count

if __name__=='__main__':
    root=Node(0)
    root.left=Node(1)
    root.right=Node(0)
    root.right.left=Node(1)
    root.right.right=Node(0)
    root.right.left.left=Node(1)
    root.right.left.right=Node(1)
    # root.printTree()
    print(count_univals(root))
    #5
