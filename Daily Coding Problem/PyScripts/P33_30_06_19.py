'''
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2

Created on 03-Jul-2019

@author: Lenovo
'''
def median(arr):
    temp_arr=[]
    for i in arr:
        temp_arr.append(i)
        temp_arr.sort()
        if len(temp_arr)==1:
            print(temp_arr[0])
        elif len(temp_arr)%2==0:
            mid=round(len(temp_arr)/2)            
            print((temp_arr[mid]+temp_arr[mid-1])/2)
        else:
            mid=round(len(temp_arr)/2)-1
            print(temp_arr[mid])
            
         
def main():
    median([2, 1, 5, 7, 2, 0, 5])

if __name__ == '__main__':
    main()