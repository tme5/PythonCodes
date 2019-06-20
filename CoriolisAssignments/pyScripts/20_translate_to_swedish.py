#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Date: 18-06-2019
Created By: TusharM

20) Represent a small bilingual lexicon as a Python dictionary in the following fashion and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
'''

def translate_to_swedish(inp):
    '''Converts the English Christmas card message to Swedish using small biligual lexicon Python dictionary
    Time complexity of this function in worst condition is O(n)'''
    trans_dict={'merry':'god', 'christmas':'jul', 'and':'och', 'happy':'gott', 'new':'nytt', 'year':'år'}
    ret_list=[]
    temp=inp.split(' ')
    for word in temp:
        if word in trans_dict.keys():
            ret_list.extend([trans_dict.get(word),' '])
        else:
            ret_list.extend([word,' '])
    return ''.join(ret_list)

if __name__=='__main__':
    print(translate_to_swedish('merry christmas and happy new year'))

    
