#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

35) The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced and understood by those who transmit and receive voice messages by radio or telephone regardless of their native language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word spoken.
'''

# py -m pip install pywin32
import win32com.client as wincl
from time import sleep
speak=wincl.Dispatch('SAPI.SpVoice') 

def speak_ICAO(message,char_pause=0.01,word_pause=0.5):
    '''Converts the message to ICAO words and text to speech power
    Time complexity of this function in worst condition is O(n^2)'''
    ICAO_dict = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    def convert(char_list):
        return [ICAO_dict.get(x.lower()) for x in char_list]
    words=message.split(' ')
    to_speak=[]
    for word in words:
        char_list=word[0:]
        to_speak.append(convert(char_list))
    for word in to_speak:
        for msg in word:
            speak.Speak(msg)
            sleep(char_pause)
        sleep(word_pause)
        

if __name__=='__main__':
    speak_ICAO('Hello Tushar')
