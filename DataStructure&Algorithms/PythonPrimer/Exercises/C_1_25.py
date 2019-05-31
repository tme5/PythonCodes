'''
Created on Apr 2, 2019

@author: TME5
'''
import re,string
def remPunctuation(strn):
    return re.sub('['+string.punctuation+']','',strn) 

strn="Let's try, Mike."
print(remPunctuation(strn))
