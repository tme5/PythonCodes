from tree import Tree
pokemons=['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon', 'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask'
]

def get_branches(data_tree,identifier):
    branch=[]
    branch.append(identifier)
    queue = data_tree[identifier].children()
    while queue:
        branch.append(queue[0])
        expansion = data_tree[queue[0]].children()
        queue = expansion + queue[1:]
    
def play_pokemon(org_pokemon):
    data_tree=Tree()
    pokemons_copy=pokemons.copy()
    data_tree.add_node(org_pokemon)
    parent_list=[org_pokemon]
    while True:
        for current_parent in parent_list:
            pokemons_copy.pop(pokemons_copy.index(current_parent))
            child_list=[x for x in pokemons_copy if x.startswith(current_parent[-1])]
            for child in child_list:
                data_tree.add_node(child,current_parent)
        parent_list=child_list
        if parent_list==[]:
            break
    
    for node in data_tree.traverse(org_pokemon, mode=1):
        print(node)
    
#     _longest=[]
#     _prev_list=[]
#     while True:
#         _parent_list=[org_pokemon]
#         i=0
#         while i<len(_parent_list):
#             current_root=_parent_list[i]
#             child_list=data_tree[current_root].children()
#             if len(child_list)>0:
#                 for child in child_list:
#                     if child not in _prev_list:
#                         _parent_list.append(child)
#                         i+=1
#                         break
#                     else:
#                         next
#             else:
#                 break
#         _prev_list=_parent_list
#         if len(_prev_list)>len(_longest):
#             _longest=_prev_list
#         if len(_parent_list)<1:
#             print(_longest)
#             break
        
if __name__=='__main__':
    play_pokemon('bagon')