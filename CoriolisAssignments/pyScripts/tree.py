#!python
'''
Created on Jun 4, 2019

@author: TME5
'''
# +---{ Import Section }---+

# +---{Supportive Class Section }---+

class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children=[]

    def identifier(self):
        return self.__identifier
        
    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)
    
(_ROOT, _DEPTH, _BREADTH) = range(3)

class Tree:

    def __init__(self):
        self.__nodes = {}

    def nodes(self):
        return self.__nodes
    
    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            #print(parent)
            self[parent].add_child(identifier)
        return node
    
    def traverse(self, identifier, mode=_DEPTH):
        # Python generator. Loosly based on an algorithm from 
        # 'Essential LISP' by John R. Anderson, Albert T. Corbett, 
        # and Brian J. Reiser, page 239-241
        yield identifier
        queue = self[identifier].children()
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children()
            if mode == _DEPTH:
                queue = expansion + queue[1:]  # depth-first
            elif mode == _BREADTH:
                queue = queue[1:] + expansion  # width-first
                
    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item
        
