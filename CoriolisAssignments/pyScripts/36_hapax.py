#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

36) A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.'''
import re

def hapax_function(path):
    '''Returns the list of all hapaxes in the file path
    Time complexity of this function in worst condition is O(n)'''
    with open(path,'r') as f:
        list_of_words = re.findall('\w+', f.read().lower())
    freqs = {key: 0 for key in list_of_words}
    for word in list_of_words:
        freqs[word] += 1
    ret_val=[]
    for word in freqs:
        if freqs[word] == 1:
            ret_val.append(word)
    return ret_val

if __name__=='__main__':
    print(hapax_function('hapax.txt'))