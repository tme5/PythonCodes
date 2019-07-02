'''
This problem was asked by Palantir.
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

Created on 28-Jun-2019

@author: Lenovo
'''
def make_sentence(sent,k):
    def add_space(num):
        sent[num]=sent[num]+' '
        return sent
    total_len=sum([len(word) for word in sent])
    i=0
    while total_len<k:
        if i<len(sent)-1:
            sent=add_space(i)
            i+=1
        else:
            i=0
        total_len=sum([len(word) for word in sent])
    return sent
    
def justify(word_list,k):
    sent_in=[]
    lst=[]
    while True:
        if len(word_list)==0:
            sent_in.append(lst)
            lst=[]
            break
        else:
            word=word_list[0]
            if sum(map(len,lst))+len(lst)+len(word)>k:
                sent_in.append(lst)
                lst=[]
            else:
                lst.append(word_list.pop(0))
    sentences=[''.join(make_sentence(sent,k)) for sent in sent_in]      
    return sentences
    
def main():
    word_list=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert justify(word_list,16)==["the  quick brown","fox  jumps  over","the   lazy   dog"], 'Wrong sentence justification'

if __name__=='__main__':
    main()
    