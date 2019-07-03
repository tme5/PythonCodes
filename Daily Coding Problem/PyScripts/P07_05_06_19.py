#!python
'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.

Created on Jun 5, 2019

@author: Administrator
'''
import string
alpha_list=list(string.ascii_lowercase)

def decode(data,k,decode_cache):
    # If we have the cache value, then return it
    if data in decode_cache:
        return decode_cache[data]    
    #Compute the rest
    if k==0:
        return 1
    s=len(data)-k
    if data[s]=='0':
        return 0
    result=decode(data,k-1,decode_cache)
    if k>=2 and int(data[s:s+2])<=26:
        result+=decode(data,k-2,decode_cache)
    decode_cache[k]=result
    return result
            
def main():
    en_msg='111111'
    decode_cache={}
    assert decode(en_msg,len(en_msg),decode_cache)==13, 'Wrong output'
          
if __name__ == '__main__': main()
