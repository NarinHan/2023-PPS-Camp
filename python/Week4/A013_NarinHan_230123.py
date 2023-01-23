'''
    A013 Single Number
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.
    https://leetcode.com/problems/single-number/
'''

nums = input().split(",")
for num in nums :
    if nums.count(num) == 1 :
        print(num)