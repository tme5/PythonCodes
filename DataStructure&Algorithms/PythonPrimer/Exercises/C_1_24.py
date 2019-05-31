'''
Created on Apr 2, 2019

@author: TME5
'''
# def countVowels(str):
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     count=0
#     for c in str:
#         if c in vowels:
#             count+=1
#     return count

def countVowels(str):
    return sum([1 for x in str if x in ['a','e','i','o','u','A','E','I','O','U']])

print(countVowels('Tushar Mangale IS AWESOME'))