#!python
'''
Created on Apr 4, 2019

@author: TME5
'''
# +---{ Import Section }---+
import time
import enchant,itertools
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

def getPermutations(data,word_len):
    ret=[]
    comb_list=itertools.permutations(data,word_len)
    for word in comb_list:
        word=''.join(word)
        ret.append(word)
    return ret
    
def getWords(data):
    d = enchant.Dict("en_US")
    word_len=1
    words=[]
    while word_len < len(data):
        words=getPermutations(data,word_len)
        word_len+=1
        words_set=set(words)
        for word in words_set:
            if d.check(word):
                yield word
    
# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    lst=['o','g','r','e','r']
    for words in getWords(lst):
        print(words,end=',')
    
if __name__ == '__main__': main()