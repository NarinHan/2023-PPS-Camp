'''
    A025 Power of Four
    Given an integer n, return true if it is a power of four.
    Otherwise, return false.
'''

n = int(input())
while True :
    if n % 4 == 0 :
        n /= 4
    else :
        ans = False
        break
    if n == 1 :
        ans = True
        break
    
print(ans)