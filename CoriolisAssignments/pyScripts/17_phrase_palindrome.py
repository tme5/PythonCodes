#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

17) Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
'''

def is_phrase_palindrome(inp):
    '''Check if input string in palindrome or not, Return True if palindrome else False
    Time complexity of this function in worst condition is O(n)'''
    if type(inp)==str:
        temp=[x for x in inp if x.isalpha()]
        #print(temp)
        while len(temp)>1:
            if temp.pop().lower() != temp.pop(0).lower():
                return False
        return True
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(is_phrase_palindrome("Go hang a salami I'm a lasagna hog."))
    #True
    print(is_phrase_palindrome("Was it a rat I saw?"))
    #True
    print(is_phrase_palindrome("Step on no pets"))
    #True
    print(is_phrase_palindrome("Sit on a potato pan, Otis"))
    #True
    print(is_phrase_palindrome("Lisa Bonet ate no basil"))
    #True
    print(is_phrase_palindrome("Satan, oscillate my metallic sonatas"))
    #True
    print(is_phrase_palindrome("I roamed under it as a tired nude Maori"))
    #True
    print(is_phrase_palindrome("Rise to vote sir"))
    #True
    print(is_phrase_palindrome("Dammit, I'm mad!"))
    #True
    
