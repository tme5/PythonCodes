'''
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

Created on 25-Jun-2019

@author: Lenovo
'''
import re

def mis_nest(inp):
    while len(inp)>0:
        org_len=len(inp)
        inp=re.sub(r'\[\]','',inp)
        inp=re.sub(r'\(\)','',inp)
        inp=re.sub(r'\{\}','',inp)
        if len(inp)==org_len:
            break
        
    if len(inp)>0:
        return False
    return True

if __name__=='__main__':
    print(mis_nest('([])[]({})'))
    #True
    print(mis_nest('([)]'))
    #False
    print(mis_nest('((()'))
    #False
    