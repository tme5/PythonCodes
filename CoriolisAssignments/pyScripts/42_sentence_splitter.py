#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM
42) A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "." (periods), "?" or "!", except that

Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
Periods followed by a digit with no intervening whitespace are not sentence boundaries.
Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
'''
import re

def sentence_splitter(file_path):
    '''Returns sentences by adding new line symbol in the text from the file path.
    Time complexity of the function is O(1)
    '''
    with open(file_path,'r') as f:
        text=f.read()
    sent=re.sub(r'\n','',text)
    sent=re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sent)
    sent=re.sub(r'\?\s',r'?\n',sent)
    sent=re.sub(r'!\s',r'!\n',sent)
    return sent 

if __name__=='__main__':
    print(sentence_splitter('sentence_splitter.txt'))