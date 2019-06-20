#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM

34) Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.
'''
def char_freq_table(file):
    '''prints the semordnilap pairs present in the file'''
    with open(file,'r') as f:
        f_rd=f.read()
        f_cl=[x.strip() for x in f_rd]
    unq=set(x for x in f_cl if x.isalpha())
    unq=sorted(unq,reverse=False)
    ret_dict={x:0 for x in unq}
    for inp in f_cl:
        lst=[x for x in inp if x.isalpha()]
        for char in lst:
            ret_dict[char]=ret_dict.get(char)+1
    return ret_dict

if __name__=='__main__':
    my_dict=char_freq_table('palindrome_input.txt')
    for k,v in my_dict.items():
        print(k,'|',v)
#     B | 1
#     D | 1
#     G | 1
#     I | 5
#     L | 1
#     M | 1
#     O | 1
#     R | 1
#     S | 3
#     W | 1
#     a | 30
#     b | 1
#     c | 4
#     d | 5
#     e | 13
#     g | 4
#     h | 2
#     i | 15
#     l | 9
#     m | 9
#     n | 13
#     o | 16
#     p | 4
#     r | 6
#     s | 14
#     t | 19
#     u | 2
#     v | 2
#     w | 1
#     y | 2
