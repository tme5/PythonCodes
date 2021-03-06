#!/usr/bin/python
'''
Date: 19-06-2019
Created By: TusharM
45) A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a word in the category, they fall out of the game. For example, with "animals" as the category,

Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final letter of the preceding name. No Pokemon name is to be repeated.

audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask
'''

import random

pokemons=['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon', 'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask'
]

def play_pokemon_old():
    pokemons_copy=pokemons.copy()
    rand_num=random.randint(0,len(pokemons))
    pokemon=pokemons_copy.pop(rand_num)
    i=1
    print(f'Player {i}: {pokemon}')
    while True:        
        next_list=[x for x in pokemons_copy if x.startswith(pokemon[-1])]
        if len(next_list)>0:
            if i==1:
                i=2
            else:
                i=1
            pokemon=pokemons_copy.pop(pokemons_copy.index(next_list[0]))
            print(f'Player {i}: {pokemon}')
        else:
            break
        
def play_pokemon_1(pokemon):
    pokemons_copy=pokemons.copy()
    pokemon=pokemons_copy.pop(pokemons_copy.index(pokemon))
    i=1
    ret_list=[pokemon]
    while True:        
        next_list=[x for x in pokemons_copy if x.startswith(pokemon[-1])]
        if len(next_list)>0:
            if i==1:
                i=2
            else:
                i=1
            pokemon=pokemons_copy.pop(pokemons_copy.index(next_list[0]))
            ret_list.append(pokemon)
        else:
            break
    return ret_list
                
if __name__=='__main__':
    longest=[]
    current=[]
    for pokemon in pokemons:
        current=play_pokemon_1(pokemon)
        if len(current)>len(longest):
            longest=current
     
    print(len(longest))     
    print(longest)
#         