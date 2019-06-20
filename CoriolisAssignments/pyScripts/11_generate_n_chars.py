#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

11) Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (pyScripts is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
'''
def generate_n_chars(count,char):
    '''Returns a string n character long consisting of only c
    Time complexity of this function in worst condition is O(n)'''
    ret_val=[]
    if type(char)==str:
        i=0
        while i<count:
            ret_val.append(char)
            i+=1
        return ''.join(ret_val)
    else:
        raise Exception('Expected count and character as input')

if __name__=='__main__':
    print(generate_n_chars(5,'x'))
    #xxxxx
    print(generate_n_chars(10,'!'))
    #!!!!!!!!!!
    print(generate_n_chars(1,'+'))
    #+
    print(generate_n_chars(0,'A'))
    #    
