#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Date: 19-06-2019
Created By: TusharM

30) Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.
'''

def translate_to_swedish(inp):
    '''Converts the English Christmas card message to Swedish using small biligual lexicon Python dictionary
    Time complexity of this function in worst condition is O(1)'''
    trans_dict={'merry':'god', 'christmas':'jul', 'and':'och', 'happy':'gott', 'new':'nytt', 'year':'år'}
    return ' '.join(list(map(lambda word: (trans_dict.get(word)) if word in trans_dict.keys() else word,inp.split(' '))))

if __name__=='__main__':
    print(translate_to_swedish('merry christmas and happy new year'))
