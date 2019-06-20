#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

24) The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith().
'''

def make_3sg_form(inp):
    '''Assuming that in the input string is first person singular form, the function converts to third person singular form.
    Time complexity of this function in worst condition is O(1)'''
    if type(inp)==str:
        if inp.endswith('y'):
            ret_val=(inp[::-1].replace('y'[::-1],'ies'[::-1],1))[::-1]
        elif inp.endswith('o') or inp.endswith('ch') or inp.endswith('s') or inp.endswith('sh') or inp.endswith('x') or inp.endswith('z'):
            ret_val=inp+'es'
        else:
            ret_val=inp+'s'
        return ret_val
    else:
        raise Exception('Input expected string')

if __name__=='__main__':
    print(make_3sg_form("run"))
    #runs
    print(make_3sg_form("match"))
    #matches
    print(make_3sg_form("body"))
    #bodies
    print(make_3sg_form("yummy"))
    #yummies
    print(make_3sg_form("fish"))
    #fishes
    print(make_3sg_form("motor"))
    #motors
    print(make_3sg_form("flux"))
    #fluxes
    print(make_3sg_form('try'))
    #tries
    print(make_3sg_form('brush'))
    #brushes
    print(make_3sg_form('fix'))
    #fixes
    