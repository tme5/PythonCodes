#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM
46) An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".
Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.
'''
with open('unixdict.txt','r') as f:
    f_rd=f.readlines()
    wordlist=[x.strip() for x in f_rd]

def all_char_in(word1,master):
    temp=list(word1)
    temp_master=list(master)
    for char in word1:
        if char not in temp_master:
            return False
        else:
            temp_master.pop(temp_master.index(char))
            temp.pop(temp.index(char))
    if len(temp)>0:
        return False
    return True

def popchars(word1,master):
    ret_val=list(master)
    for char in word1:
        ret_val.pop(ret_val.index(char))
    return ''.join(ret_val)

import collections
alternade_dict=collections.defaultdict(list)
for word in wordlist:
    first_words=[]
    second_words=[]
    word_len=len(word)
    if word_len>2:
        first_char=word[0]
        wordlist_1=list(filter(lambda x: len(x)<word_len,wordlist))
        first_words=list(filter(lambda x: x.lower().startswith(first_char), wordlist_1))
        second_char=word[1]
        second_words=list(filter(lambda x: x.lower().startswith(second_char), wordlist_1))
        if len(first_words)>0 and len(second_words)>0:
            for first_word in first_words:
                if all_char_in(first_word,word):
                    temp_word=popchars(first_word,word)
                    for second_word in second_words:
                        if len(second_word)==len(temp_word) and all_char_in(second_word,temp_word) and len(first_word)>len(second_word):
                            alternade_dict[word].append([first_word,second_word])
                            print(f'"{word}": makes "{first_word}" and "{second_word}"')


                            
                            
                            