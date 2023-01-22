'''
    A122 Rotate String
    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the rightmost position.
    https://leetcode.com/problems/rotate-string/
'''

s = list(input())
goal = input()
ans = False
for _ in range(len(s)) :
    temp = s[0]
    s.remove(s[0])
    s.append(temp)
    if "".join(s) == goal :
        ans = True
        break
print(ans)