file='V:\\R29SP2\\Perf_Impact_Automation\\!101474!Case3ApiRayFire.scm.time_res.txt'

with open(file,'r') as f:
    f_rd=f.readlines()
    f_cl=[x.strip() for x in f_rd]
    

from pythonScripts.tree import Tree

_CALL_DEPTH=7
_parent_list=list(range(1,_CALL_DEPTH,1))
data_tree=Tree()

for line in f_cl:
    data=line.split(',')
    _cur_level=int(data[0])
    if _cur_level<=_CALL_DEPTH:
        if _cur_level==2:
            data_tree.add_node(data[1], [data[0],data[2],data[3]])
            _parent_list[0]=data[1]            
        else:
            #print(_parent_list[_cur_level-3])
            data_tree.add_node(data[1], [data[0],data[2],data[3]], _parent_list[_cur_level-3])
            _parent_list[_cur_level-2]=data[1]

#+----{ Get Favourite child }----+
def fav_child(root):
    max_time=0.00
    call_count=0
    call_depth=0
    fav_child=None
    for child in root.children():
        child_data=data_tree[child].data()
        if float(child_data[1]) > float(max_time):
            max_time=child_data[1]
            call_count=child_data[2]
            call_depth=child_data[0]
            fav_child=child
    return [fav_child,call_depth,max_time,call_count]

root=data_tree['rayfire_entitylist']
ray_culprit=[]
ray_culprit.append(['rayfire_entitylist',root.data()[0],root.data()[1],root.data()[2]])
cur_parent='rayfire_entitylist'
while True:
    if len(data_tree[cur_parent].children())==0:
        break
    level_fav_child=fav_child(data_tree[cur_parent])
    ray_culprit.append(level_fav_child)
    cur_parent=level_fav_child[0]

print(len(ray_culprit))
print(ray_culprit)
      


            