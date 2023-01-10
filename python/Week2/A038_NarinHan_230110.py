'''
    A038 Sqrt(x)
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.
    Do not use any built-in exponent function or operator.
    https://leetcode.com/problems/sqrtx/
'''

x = int(input())

for i in range(x) :
    if i * i == x :
        ans = i
        break
    elif i * i > x :
        ans = i - 1
        break
    else :
        continue

print(ans)