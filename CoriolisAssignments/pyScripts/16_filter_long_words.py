#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM
16) Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
'''

def filter_long_words(lst,length):
    '''Returns a list of words from the input list which are longer than the length given
    Time complexity of the function is O(n)'''
    if length>=0:
        ret_list=[]
        for word in lst:
            if type(word)==str:
                if len(word)>length:
                    ret_list.append(word)
            else:
                raise Exception('Expected list of Strings')
        return ret_list
    else:
        raise Exception('Expected positive length')


if __name__=='__main__':
    print(filter_long_words.__doc__)
    # Get the docstring of the function
    print(filter_long_words(['tushar','python','example','I','am'],2))
    #['tushar', 'python', 'example']
    print(filter_long_words(['tushar','python','example','I','am'],7))
    #[]
    print(filter_long_words(['tushar','python','example','I','am'],0))
    #['tushar', 'python', 'example', 'I', 'am']
    #print(filter_long_words(['tushar','python','example','I','am'],-1))
    #Exception
    