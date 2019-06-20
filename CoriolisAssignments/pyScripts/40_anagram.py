#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

40) An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:

>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
'''
import random
colors=['red','green','blue','yellow','black','white','orange','violet','purple','pink','brown']
#Choose a random color
color_index=random.randint(1,len(colors))
color_chosen=colors[color_index]
temp_color=list(color_chosen)
random.shuffle(temp_color)
shuffled_color=''.join(temp_color)
print(f'Color word anagram: {shuffled_color}')
while True:
    user_guess=input('Guess the color word!\n')
    if user_guess==color_chosen:
        print('Correct')
        break
