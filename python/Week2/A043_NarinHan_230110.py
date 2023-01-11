'''
    A043 Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string.
    https://leetcode.com/problems/longest-common-prefix/
'''

words = input().split()

short = min(words, key=len)

for w in words :
    while len(short) > 0 :
        if w.startswith(short) :
            break
        else :
            short = short[:-1]
    
print(short)