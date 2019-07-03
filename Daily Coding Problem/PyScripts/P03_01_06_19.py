'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

Created on Jun 3, 2019

@author: Administrator
'''
class Node:
    def __init__(self,val,left=None,right=None):
        self.value=val
        self.left=left
        self.right=right

def serialize(node):
    ret=[]
    def node_to_string(node):
        if node:
            ret.append(str(node.value))
            node_to_string(node.left)
            node_to_string(node.right)
        else:
            ret.append('?')
    node_to_string(node) 
    return ','.join(ret)

def deserialize(inp):
    lst=iter(inp.split(','))
    def string_to_node():
        try:
            inp=next(lst)
            if inp=='?':
                return None
            else:
                node=Node(inp)
                node.left=string_to_node()
                node.right=string_to_node()
                return node
        except StopIteration:
            pass
    return string_to_node()
    
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.value == 'left.left'

