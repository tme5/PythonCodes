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
def min_steps(matrix,start,end):
    if matrix[start[0]][start[1]]=='t' or matrix[end[0]][end[1]]=='t':
        return False
    curr_pos=start
    step=0
    if curr_pos[0]>0:
        i=-1
    else:
        i=1
    if curr_pos[1]>0:
        j=-1
    else:
        j=1
    prev_pos=start
    while curr_pos!=end:            
        next_pos=(curr_pos[0]+i,curr_pos[1])
        if matrix[next_pos[0]][next_pos[1]]=='f':
            curr_pos=next_pos
            step+=1
        else:
            curr_pos=(curr_pos[0],curr_pos[1]+j)
            step+=1
        if curr_pos[0]>=prev_pos[0]:
            i=1
        else:
            i=-1
        if curr_pos[1]>=prev_pos[1]:
            j=1
        else:
            j=-1   
        prev_pos=curr_pos
            
matrix=[['f', 'f', 'f', 'f'],
['t', 't', 'f', 't'],
['f', 'f', 'f', 'f'],
['f', 'f', 'f', 'f']]
start=(3,0)
end=(0,0)
print(min_steps(matrix,start,end))