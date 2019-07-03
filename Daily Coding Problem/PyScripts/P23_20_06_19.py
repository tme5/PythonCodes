'''
This problem was asked by Google.
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

Created on 25-Jun-2019

@author: Lenovo
'''
def mark_adjacent(matrix, pos,num):
    crow=len(matrix)
    ccol=len(matrix[0])
    ret_list=[]
    adjs=[(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]
    for adj in adjs:
        if adj[0]<crow and adj[0]>=0 and adj[1]<ccol and adj[1]>=0 and matrix[adj[0]][adj[1]]!='t' and type(matrix[adj[0]][adj[1]])!=int:
            matrix[adj[0]][adj[1]]=num
            ret_list.append(adj)
    return ret_list          
                
def main():
    matrix=[['f', 'f', 'f', 'f'],
    ['t', 't', 'f', 't'],
    ['f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f']]
    start=(3,0)
    end=(0,0)
    if matrix[start[0]][start[1]]=='t' or matrix[end[0]][end[1]]=='t':
        print('No Solution')
    else:
        num=0
        matrix[start[0]][start[1]]=num
        adj=[start]
        while end not in adj:
            num+=1
            ret_val=[]
            for pos in adj:
                ret_val.extend(mark_adjacent(matrix, pos, num))
            adj=ret_val
        assert matrix[end[0]][end[1]]==7, 'Wrong output'

if __name__=='__main__':
    main()