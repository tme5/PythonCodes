'''
This problem was asked by Facebook.
Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

Created on 25-Jun-2019

@author: Lenovo
'''
def regex(inp,ex):
    str=list(inp)
    rexp=list(ex)
    while len(rexp)>0:
        char=rexp[0]
        if char!='*':
            if char=='.':
                str.pop(0)
                rexp.pop(0)
            if char.isalpha():
                if str.pop(0)!=rexp.pop(0):
                    return False
        else:
            rexp.pop(0)
            while True:
                if ''.join(str).startswith(''.join(rexp)):
                    break
                else:
                    str.pop(0)
    if len(str)>0:
        return False
    return True

def main():
    assert regex('ray','ra.')==True, 'Passing case'
    assert regex('raymond','ra.')==False, 'Failing case'
    assert regex('cheaat','.*at')==True, 'Passing case'
    assert regex('chats','*at')==False, 'Passing case'
    
if __name__=='__main__':
    main()