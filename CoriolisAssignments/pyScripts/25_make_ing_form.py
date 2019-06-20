#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

25) In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
'''

def make_3sg_form(inp):
    '''Assuming that in the input string is a verb, the function converts to present participles.
    Time complexity of this function in worst condition is O(1)'''
    vowels=['a','e','i','o','u']
    e_exceptions=['be','see','flee','knee']
    if type(inp)==str:
        if inp.endswith('e'):
            if inp.endswith('ie'):
                ret_val=(inp[::-1].replace('ie'[::-1],'ying'[::-1],1))[::-1]
            elif inp in e_exceptions:
                ret_val=inp+'ing'
            else:
                ret_val=(inp[::-1].replace('e'[::-1],'ing'[::-1],1))[::-1]
        else:
            if inp[-1] not in vowels and inp[-2] in vowels and inp[-3] not in vowels:
                ret_val=inp+inp[-1]+'ing'
            else:
                ret_val=inp+'ing'
        return ret_val
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(make_3sg_form("go"))
    #going
    print(make_3sg_form("lie"))
    #lying
    print(make_3sg_form("see"))
    #seeing
    print(make_3sg_form("move"))
    #moving
    print(make_3sg_form("hug"))
    #hugging
    print(make_3sg_form("be"))
    #being
    print(make_3sg_form("see"))
    #seeing
    print(make_3sg_form('flee'))
    #fleeing
    print(make_3sg_form('knee'))
    #kneeing
    