#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

5) Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon"
'''

def translate(inp):
    '''Translate the input string into "rövarspråket" (Swedish robber's language)
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        escape_chars=['a','e','i','o','u']
        ret_val=[]
        for char in inp:
            if char.lower() not in escape_chars and char.isalpha():
                ret_val.extend([char,'o',char])
            else:
                ret_val.append(char)                
        return ''.join(ret_val)
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(translate('this is fun'))
    #tothohisos isos fofunon
    print(translate('this, is fun.!#'))
    #tothohisos, isos fofunon.!#
    
