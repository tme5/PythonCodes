#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

18) A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
'''
import string
def is_pangram(inp):
    '''Check if input string in pangram or not, Return True if pangram else False. Considers only alphabets
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        temp=set(x.lower() for x in inp if x.isalpha())
        temp=sorted(temp,reverse=False)
        #print(temp)
        if temp==sorted(set(string.ascii_lowercase)):
            return True
        return False
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
    #True
    print(is_pangram("Go hang a salami I'm a lasagna hog."))
    #False
    print(is_pangram("Was it a rat I saw?"))
    #False

    
