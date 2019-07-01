'''
This problem was asked by Google.
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

Created on 25-Jun-2019

@author: Lenovo
'''
class Node:
    def __init__(self,data,identifier=None):
        self.identifier=identifier
        self.val=data
        self.right=None
        self.left=None
        self.locked=False
        self.locked_descendants=0
    
    def _can_lock_or_unlock(self):
        if self.locked_descendants>0:
            return False
        cur=self.identifier
        while cur:
            if cur.locked:
                return False
            cur=cur.identifier
        return True
        
    def is_locked(self):
        return self.locked
    
    def lock(self):
        if self._can_lock_or_unlock():
            self.locked=True
            cur=self.identifier
            while cur:
                cur.locked_descendants+=1
                cur=cur.identifier
            return True
        else:
            return False
        
    def unlock(self):
        if self._can_lock_or_unlock():
            self.locked=False
            cur=self.identifier
            while cur:
                cur.locked_descendants-=1
                cur=cur.identifier
            return True
        else:
            return False

def main():
    root=Node(1)
    root.left=Node(2,root)
    root.left.left=Node(4,root.left)
    root.left.left.left=Node(8,root.left.left)
    root.left.left.right=Node(9,root.left.left)
    root.left.right=Node(5,root.left)
    root.left.right.left=Node(10,root.left.right)
    root.left.right.right=Node(11,root.left.right)
    root.right=Node(3,root)
    root.right.left=Node(6,root.right)
    root.right.left.right=Node(13,root.right.left)
    root.right.right=Node(7,root.right)
    root.right.right.left=Node(14,root.right.right)
    
    assert root.lock()==True, 'Can\'t Lock Node'
    assert root.unlock()==True, 'Can\'t unlock Node'
    assert root.is_locked()==False,'Unexpected status'
    assert root.right.right.left.is_locked()==False, 'Unexpected status'
    assert root.right.right.left.lock()==True, 'Can\'t Lock Node'
    assert root.right.lock()==False, 'Shouldn\'t Lock Node'
    assert root.right.right.left.unlock()==True, 'Can\'t unlock Node'
    assert root.right.lock()==True, 'Can\'t Lock Node'
    
    

if __name__=='__main__':
    main()