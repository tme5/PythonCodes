from collections import defaultdict
import functools
pokemons=['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon', 'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask'
]

def make_dict(words):
    ret_dict = defaultdict(set)
    for word in words:
        ret_dict[word[0]].add(word)
    return ret_dict
 
def longest_branch(mydict, cur_lst):
    last_char= cur_lst[-1][-1]
    rest = mydict[last_char] - set(cur_lst)
    if not rest:
        return cur_lst
    else:
        alternatives = [longest_branch(mydict,list(cur_lst)+[word]) for word in rest]
        mx = functools.reduce(lambda a,b: a if len(a)>len(b) else b,alternatives)
        return mx
 
def play_pokemon(words): 
    poke_dict = make_dict(words)
    longest=[]
    current=[]
    for word in words:
        current=longest_branch(poke_dict,[word])
        if len(current)>len(longest):
            longest=current
    return longest
 
if __name__ == '__main__':
    pokemons = sorted(set(pokemons))    
    longest = play_pokemon(pokemons)
    print(len(longest))
    for pok in longest:
        print(pok,end=' ')
    print('\n')
    