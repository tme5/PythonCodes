#!python
'''
Created on Jun 4, 2019

@author: TME5
'''
# +---{ Import Section }---+
import sys,os,time
# +---{Supportive Class Section }---+
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1)} s')
    return wrapper

def parse(file):
    with open(file,'r') as f:
        f_rd=f.readlines()
        f_cl=[x.strip() for x in f_rd]
    
    tree_data=[]
    for line in f_cl:
        arr=line.split('\t')
        if int(arr[0])!=0:
            if str(arr[2])=='Flat Profiling Results.':
                return tree_data
            else:
                tree_data.append([int(arr[0]),arr[2],abs(float(arr[5])),int(arr[4])])
    return tree_data

# +---{ Main Section }---+
@elapsed_time
def main():
    """
    main function
    """
    fpath='\\\\Storagespaplp\\acis\\QA\\R29SP2\\Perf_Impact_Automation'
    with open(fpath+'\\timeFiles.list','r') as f:
        f_rd=f.readlines()
        time_files=[x.strip() for x in f_rd]
    for file in time_files:
        tree_data=parse(file)
        print(len(tree_data))
        perf_culprit=[]
        rayfire_entitylist=[]
        flag=False
        max_time=0.00
        for data in tree_data:
            if data[0]==2:
                flag=False
                #print(type(float(data[2])))
                if data[2] > max_time:
                    max_time=data[2]
                    perf_culprit=data
            if data[0]==2 and data[1]=='rayfire_entitylist':
                flag=True
            if flag:
                rayfire_entitylist.append(data)
           
        from tree import Tree
        
        _CALL_DEPTH=7
        _parent_list=list(range(1,_CALL_DEPTH,1))
        data_tree=Tree()
        
        for data in rayfire_entitylist:
            #data=line.split(',')
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
        
        #print(ray_culprit)
        rest_ray_children_data=[]
        last_ray_cul=ray_culprit[-1]
        parent_n_1=ray_culprit[_CALL_DEPTH-3][0]
        #print(penultimate_parent)
        last_children=data_tree[parent_n_1].children()
        for child in last_children:
            child_data=data_tree[child].data()
            child_data.insert(0,child)
            #print(child_data[2])
            if child_data[0]!=last_ray_cul[0] and child_data[2]>0.0000: 
                rest_ray_children_data.append(child_data)
        
        #+----{ Overall result }----+
        if perf_culprit[1]!='rayfire_entitylist':
            with open(fpath+'\\Overall_res.txt','a') as f:
                f.write(file+','+'Not Valid\n')
        else:
            with open(fpath+'\\Overall_res.txt','a') as f:
                f.write(file+','+last_ray_cul[0]+'\n')
        
        #+----{ Individual detail report }----+
        with open(file+'_res.txt','w') as f:
            f.write("Worst Performance\n\n")
            for data in ray_culprit:
                f.write(str(data[0])+','+str(data[1])+','+str(data[2])+','+str(data[3])+'\n')
            f.write(f"\nRest Call Depth {_CALL_DEPTH} API info\n\n")
            for data in rest_ray_children_data:
                f.write(str(data[0])+','+str(data[1])+','+str(data[2])+','+str(data[3])+'\n')
            
if __name__ == '__main__': main()