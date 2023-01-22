'''
    A103 Unique Morse Code Words
    International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes.
    Given an array of strings 'words' where each word can be written as a concatenation of the Morse code of each letter.
    Return the number of different transformations among all words we have.
    https://leetcode.com/problems/unique-morse-code-words/
'''

import string

alpha = list(string.ascii_lowercase)
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
d = dict(zip(alpha, morse)) # key=알파벳 value=모스 부호로 딕셔너리로 생성
d['"'] = '"'

words = list(map(str, input().split(",")))
ans = list()
for w in words :
    temp = ""
    for ch in w :
        temp += d[ch]
    ans.append(temp)
print(len(set(ans))) # unique 결과들만 남겨서 개수 출력