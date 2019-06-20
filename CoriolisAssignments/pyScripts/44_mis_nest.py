#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM
44) Your task in this exercise is as follows:

Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
'''
import re

def mis_nest(inp):
    while len(inp)>0:
        org_len=len(inp)
        inp=re.sub(r'\[\]','',inp)
        if len(inp)==org_len:
            break
        
    if len(inp)>0:
        return False
    return True
        

if __name__=='__main__':
    print(mis_nest('[]'))
    #True
    print(mis_nest('[][]'))
    #True
    print(mis_nest('[[][]]'))
    #True
    print(mis_nest('[[[[]]]]'))
    #True
    print(mis_nest(']['))
    #False
    print(mis_nest('][]['))
    #False
    print(mis_nest('[]][[]'))
    #False
    