'''
This problem was asked by Google.
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between "kitten" and "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".
Given two strings, compute the edit distance between them.

Created on 03-Jul-2019

@author: Lenovo
'''
def edit_distance(str1,str2):
    '''Iterative Levenshtein edit distance'''
    matrix=[[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    i=0
    while i<len(str1)+1:
        j=0
        while j<len(str2)+1:
            if i==0 and j==0:
                matrix[i][j]=0
            elif i==0:
                matrix[i][j]=j
            elif j==0:
                matrix[i][j]=i
            else:
                if str1[i-1]==str2[j-1]:
                    matrix[i][j]=matrix[i-1][j-1]
                else:
                    matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
            j+=1
        i+=1
    return matrix[-1][-1]

def main():
    assert edit_distance('benyam','ephrem')==5, 'Wrong output'
    assert edit_distance('kitten','sitting')==3, 'Wrong output'
    assert edit_distance('sitting','kitten')==3, 'Wrong output'
    assert edit_distance("Python", "Peithen")==3, 'Wrong output'
    assert edit_distance("Python", "Pethno")==3, 'Wrong output'
    assert edit_distance("flaw", "lawn")==2, 'Wrong output'
    assert edit_distance("Manhattan", "Manahaton")==3, 'Wrong output'
    
if __name__ == '__main__':
    main()