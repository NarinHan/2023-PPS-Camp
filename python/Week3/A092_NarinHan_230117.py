'''
    A092 Sort Array By Parity 2
    Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
    Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
    Return any answer array that satisfies this condition.
'''

nums = list(map(int, input().split(",")))
odd, even, ans = list(), list(), list()
for n in nums :
    if n % 2 == 0 :
        even.append(n) # 짝수 리스트 생성
    else :
        odd.append(n) # 홀수 리스트 생성
for i in range(len(nums)) :
    if i % 2 == 0 :
        ans.append(even.pop())
    else :
        ans.append(odd.pop())
print(ans)
        
