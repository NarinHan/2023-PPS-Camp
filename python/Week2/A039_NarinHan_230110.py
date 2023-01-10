'''
    A039 Valid Perfect Square
    Given a positive integer number, return true if the number is a perfect square.
    Otherwise, return false. 
    Do not use any built-in library function.
    https://leetcode.com/problems/valid-perfect-square/
'''

num = int(input())

sq = 1
ans = False
while(sq <= (num // 2)) :
    if sq * sq == num :
        ans = True
        break
    sq += 1

if num == 1 :
    ans = True

print(ans)