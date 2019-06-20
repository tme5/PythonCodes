#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM

33) According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
'''
def in_file_semordnilap(file):
    '''prints the semordnilap pairs present in the file
    Time complexity of the function is O(n)'''
    with open(file,'r') as f:
        f_rd=f.readlines()
        f_cl=[x.strip() for x in f_rd]
    ref_set=[]
    list(map(lambda x: ref_set.extend(x.split(' ')), f_cl))
    for inp in ref_set:
        rev_inp=inp[::-1]
        if rev_inp in ref_set:
            print(inp,rev_inp)


if __name__=='__main__':
    in_file_semordnilap('palindrome_input_1.txt')
#     SWAP PAWS
#     STEEL LEETS
#     LEETS STEEL
#     PEELS SLEEP
#     SERIF FIRES
#     FIRES SERIF
#     SLEEP PEELS
#     STRESSED DESSERTS
#     DEVIL LIVED
#     LIVED DEVIL
#     DESSERTS STRESSED
#     DELIVER REVILED
#     PAWS SWAP
#     REDIPS SPIDER
#     DEBUT TUBED
#     DEEPS SPEED
#     SPEED DEEPS
#     TUBED DEBUT
#     SPIDER REDIPS
#     REVILED DELIVER
#     DIAPER REPAID
#     DRAWER REWARD
#     LOOTER RETOOL
#     RETOOL LOOTER
#     MURDER REDRUM
#     REDRUM MURDER
#     REWARD DRAWER
#     REPAID DIAPER
#     ANIMAL LAMINA
#     DEPOTS STOPED
#     STOPED DEPOTS
#     LAMINA ANIMAL
    
