'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

Created on 25-Jun-2019

@author: Lenovo
'''
def longest_substring(mainstr,k):
    longest=''
    substr=''
    i=0
    j=0
    while i<len(mainstr):
        substr+=mainstr[i]
        if len(set(substr))>k:
            j+=1
            i=j
            substr=''
        else:
            longest=longest if len(longest)>len(substr) else substr
            i+=1
    return longest

def main():
    assert longest_substring('abcba',2)=='bcb', 'Wrong output'
    assert longest_substring("aabacbebebe", 3)=='cbebebe', 'Wrong output'
    
if __name__=='__main__':
    main()