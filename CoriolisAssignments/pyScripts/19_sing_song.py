#!/usr/bin/python

'''
Date: 18-06-2019
Created By: TusharM

19) "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.
Your task here is write a Python program capable of generating all the verses of the song.
'''

def sing_song():
    '''Prints the verse of the traditional song "99 Bottles of Beer"
    Time complexity of this function in worst condition is O(n)'''
    i=99
    while i>0:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
        i-=1
        print(f'Take one down, pass it around, {i} bottles of beer on the wall.')

if __name__=='__main__':
    sing_song()

    
