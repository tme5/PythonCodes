#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM

39) Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

>>> import guess_number
Hello! What is your name?
user
Well, user, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, user! You guessed my number in 3 guesses!
'''

import random

usr_name=input('Hello! What is your name?\n')
print(f'Well {usr_name}, I am thinking of a number between 1 and 20.\n')
rand_num=random.randint(1,20)
count=0
while True:
    count+=1
    usr_guess=int(input('Take a guess.\n'))
    if usr_guess<rand_num:
        print('Your guess is too low')
    elif usr_guess>rand_num:
        print('Your guess is too high')
    elif usr_guess==rand_num:
        print(f'Good job, {usr_name}! You guessed my number in {count} guesses')
        break