'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

Created on 25-Jun-2019

@author: Lenovo
'''
def autocomplete(inp,lst):
    return [word for word in lst if word.startswith(inp)]

def main():
    assert autocomplete('de', ['dog','deer','deal'])==['deer','deal'],'Wrong output' 
    
if __name__=='__main__':
    main()
    