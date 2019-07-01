'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

Created on 25-Jun-2019

@author: Lenovo
'''
from collections import defaultdict
def make_dict(words):
    ret_dict = defaultdict(set)
    for word in words:
        ret_dict[word[0]].add(word)
    return ret_dict

def sent_in_list(my_dict):
    retval=[]
    for sentence,words in my_dict.items():
        ret=[]
        def_dict=make_dict(words)
        while len(sentence)>0:
            for word in def_dict[sentence[0]]:
                if sentence.startswith(word):
                    ret.append(word)
                    sentence=sentence.replace(word,'')
        retval.append(ret)
    return retval

def main():
    my_dict={"thequickbrownfox":['quick', 'brown', 'the', 'fox'],"bedbathandbeyond":['bed', 'bath', 'bedbath', 'and', 'beyond']}
    [val1,val2]=sent_in_list(my_dict)
    assert val1==['the', 'quick', 'brown', 'fox'],'Return list doesnt match'
    assert val2==['bed', 'bath', 'and', 'beyond'] or val2==['bedbath', 'and', 'beyond'],'Return list doesnt match'
    
if __name__=='__main__':
    main()
    