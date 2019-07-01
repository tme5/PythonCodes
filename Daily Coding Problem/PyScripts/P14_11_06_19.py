'''
This problem was asked by Google.
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.

Created on 25-Jun-2019

@author: Lenovo
'''
import random

def find_pi(N=2000,r=4):
    '''
    Monte Carlo Method for finding value of pi
    n = Count of points inside the curve
    N = Total number of points
    r= input radius of circle
    Area of curve / Area of square = n/N ( Probablity of points lying inside of circle ) 
    ((pi * r**2)/4) / (r**2) = n/N
    pi = n/N * ( r**2) *4 / r**2
    pi = n/N * 4
    For getting value upto 3 decimal we have kept the default value of N as 2000
    '''
    n=0 
    i=0
    while i<N:
        x,y=random.uniform(0,r),random.uniform(0,r)
        if (x**2+y**2-r**2)<=0:
            n+=1
        i+=1
    return (n/N*4)
    
def main():
    print(find_pi(2000,16))
        
if __name__=='__main__':
    main()
    