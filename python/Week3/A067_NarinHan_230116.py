'''
    A067 Remove All Adjacent Duplicates in String
    You are given a string 's' consisting of lowercase English letters. 
    A duplicate removal consists of choosing two adjacent and equal letters and removing them.
    We repeatedly make duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made. 
    It can be proven that the answer is unique.
    https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
'''

s = input()
stack = list()
for ch in s :
    if len(stack) != 0 and ch == stack[-1] :
        stack.pop()
        continue
    stack.append(ch)
print("".join(stack))
