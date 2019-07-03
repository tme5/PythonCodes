'''
This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
Created on 25-Jun-2019

@author: Lenovo
'''
def ways_to_climb_old(tot_steps,step):
    '''Recursive Programming'''
    if tot_steps<0:
        return 0
    elif tot_steps==0:
        return 1
    elif tot_steps in step:
        return 1+sum(ways_to_climb_old(tot_steps-x, step) for x in step if x<tot_steps)
    else:
        return sum(ways_to_climb_old(tot_steps-x, step) for x in step if x<tot_steps)


def ways_to_climb(tot_steps,step):
    '''Dynamic Programming'''
    ways=[0 for x in range(tot_steps+1)]
    ways[0]=1
    for i in range(tot_steps+1):
        ways[i]+=sum(ways[i-x] for x in step if i-x>0)
        ways[i]+=1 if i in step else 0
    return ways[-1]

def main():
    assert ways_to_climb(4,{1,2})==5,'Wrong output'
    assert ways_to_climb(4,{1,2,3})==7,'Wrong output'
    
if __name__=='__main__':
    main()