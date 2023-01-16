'''
    A115 Maximum Number of Balloons
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
    You can use each character in text at most once. Return the maximum number of instances that can be formed.
    https://leetcode.com/problems/maximum-number-of-balloons/
'''

text = input()
d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
for ch in d :
    d[ch] = text.count(ch)
if d['b'] == d['a'] == d['n'] and d['l'] == d['o'] and d['b'] * 2 == d['l'] :
    print(d['b'])
else :
    print(0)
