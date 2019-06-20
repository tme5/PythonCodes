#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

38) Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
'''
import re
from _functools import reduce

def avg_word_length(path):
    '''Returns the average word length, split the word in case of punctuation
    Time complexity of this function in worst condition is O(n)'''
    with open(path,'r') as f:
        list_of_words = re.findall('\w+', f.read())
        
    #print(list_of_words)
    word_len=[]
    for word in list_of_words:
        word_len.append(len(word))
    return (reduce(lambda a,b:a+b,word_len)/len(word_len))

if __name__=='__main__':
    print(avg_word_length('avg_word_len.txt'))
    #3.1666666666666665