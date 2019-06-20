#!/usr/bin/python
'''
Date: 18-06-2019
Created By: TusharM

21) Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
'''

def char_freq(inp):
    '''Returns a dictionary of frequency of occurence of characters in the input string, considers only characters
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        unq=set(x for x in inp if x.isalpha())
        unq=sorted(unq,reverse=False)
        ret_dict={x:0 for x in unq}
        #print(temp)
        lst=[x for x in inp if x.isalpha()]
        for char in lst:
            ret_dict[char]=ret_dict.get(char)+1
    else:
        raise Exception('Input expected string')
    return ret_dict

if __name__=='__main__':
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))
    #{'a': 7, 'b': 14, 'c': 3, 'd': 3}
    print(char_freq('merry christmas and happy new year'))
    #{'a': 4, 'c': 1, 'd': 1, 'e': 3, 'h': 2, 'i': 1, 'm': 2, 'n': 2, 'p': 2, 'r': 4, 's': 2, 't': 1, 'w': 1, 'y': 3}
    
