#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM

32) Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.
'''

def in_file_palindrome(file):
    '''Check if input string in palindrome or not, Return True if palindrome else False
    Time complexity of this function in worst condition is O(n)'''
    with open(file,'r') as f:
        f_rd=f.readlines()
        f_cl=[x.strip() for x in f_rd]
    for inp in f_cl:
        temp=[x for x in inp if x.isalpha()]
        flag=True
        while len(temp)>1:
            if temp.pop().lower() != temp.pop(0).lower():
                flag=False
        if flag:
            print(inp)

if __name__=='__main__':
    in_file_palindrome('palindrome_input.txt')
#     Go hang a salami I'm a lasagna hog.
#     Was it a rat I saw?
#     Step on no pets
#     Sit on a potato pan, Otis
#     Lisa Bonet ate no basil
#     Satan, oscillate my metallic sonatas
#     I roamed under it as a tired nude Maori
#     Rise to vote sir
#     Dammit, I'm mad!
    
