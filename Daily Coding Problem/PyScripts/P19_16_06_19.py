'''
This problem was asked by Facebook.
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

Created on 25-Jun-2019

@author: Lenovo
'''
def color(inp):
    cost=[]
    for house,vals in enumerate(inp):
        if house==0:
            cost_s=min(vals)
            col_i=vals.index(cost_s)
            cost.append(cost_s)
        else:
            cp_vals=vals.copy()
            cp_vals.pop(col_i)
            cost_s=min(cp_vals)
            col_i=vals.index(cost_s)
            cost.append(cost_s)
        print(f'House {house} get color {col_i} having value {cost_s}')
    return sum(cost)

def main():
    input=[[17,2,17],[16,16,5],[14,3,19]]
    Output=color(input)
    print(f'Minimum cost is {Output}')
    assert Output==10, 'Wrong output'
    
if __name__=='__main__':
    main()