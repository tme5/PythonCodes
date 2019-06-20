#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM
43) An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
'''
import collections

def find_anagram(file_path):
    with open(file_path,'r') as f:
        words_rd=f.readlines()
        words=[x.strip() for x in words_rd]
        
    ana_dict=collections.defaultdict(list)
    
    for word in words:
        key=''.join(sorted(word))
        ana_dict[key].append(word)
    
    max_len=0
    for anagram,anaword in ana_dict.items():
        if len(anaword)>max_len:
            max_len=len(anaword)
    
    for anagram,anaword in ana_dict.items():
        if len(anaword)==max_len:
            print(anagram,'-',anaword)

if __name__=='__main__':
    find_anagram('unixdict.txt')