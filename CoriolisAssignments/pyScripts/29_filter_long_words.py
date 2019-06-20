#!/usr/bin/python

'''
Date: 19-06-2019
Created By: TusharM
29) Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
'''

def filter_long_words(lst,length):
    '''Returns a list of words from the input list which are longer than the length given
    Time complexity of the function is O(1)'''
    if length>=0:
        return list(filter(lambda x: len(x)>length,lst))
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

    