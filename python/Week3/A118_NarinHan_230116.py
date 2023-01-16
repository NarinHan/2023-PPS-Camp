'''
    A118 Move Zeroes
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.
    https://leetcode.com/problems/move-zeroes/
'''

nums = list(map(int, input().split(",")))
cnt = nums.count(0)
for n in nums :
    if n == 0 :
        nums.remove(n)
for i in range(cnt) :
    nums.append(0)
print(nums)
