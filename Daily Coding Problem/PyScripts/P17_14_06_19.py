'''
This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.

Created on 25-Jun-2019

@author: Lenovo
'''
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
    
    def get_identifier(self):
        return self.__identifier 

class Tree:
    def __init__(self):
        self.__nodes = {}
        
    def nodes(self):
        return self.__nodes
    
    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node
        if parent is not None:
            self[parent].add_child(identifier)
        return node
          
    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item

def get_path(dir_tree):
    pass
      
def longest_filepath(inp):
    lst=inp.split('\n')
    _parent_list=[]
    max_len=0
    for str in lst:
        tabs=str.count('\t')
        if tabs==0:
            _parent_list.append(str)
        elif tabs>0:
            sub=str.replace('\t', '')
            if len(_parent_list)<=tabs:
                _parent_list.append(sub)
            else:
                _parent_list[tabs]=sub
        if '.' in _parent_list[-1]:
            max_len=max(max_len,len('/'.join(_parent_list)))
    return max_len

def main():
    assert longest_filepath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')==32, 'Not the longest path'

if __name__=='__main__':
    main()