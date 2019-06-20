
#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

37) Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
'''
import re

def line_number(path):
    '''Creates a new file with same name appended with _new with all original lines prepended with line number
    Time complexity of this function in worst condition is O(n)'''
    with open(path,'r') as f:
        f_rd=f.readlines()
    new_file=path[::-1].split('.')[1][::-1]+'_new.txt'
    print(new_file)
    i=0
    with open(new_file,'w') as f:
        while i<len(f_rd):
            f.write(str(i+1)+' '+f_rd[i])
            i+=1

if __name__=='__main__':
    print(line_number('palindrome_input.txt'))