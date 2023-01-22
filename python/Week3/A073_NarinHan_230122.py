'''
    A073 Fizz Buzz
    Given an integer n, return a string array answer(1-indexed) where :
    - answer[i] == "FizzBuzz" if i is divisible by 3 and 5
    - answer[i] == "Fizz" if i is divisible by 3
    - answer[i] == "Buzz" if i is divisible by 5
    - answer[i] == i if none of the above conditions are true
    https://leetcode.com/problems/fizz-buzz/
'''

n = int(input())
nlist = [i+1 for i in range(n)]
ans = list()
for num in nlist :
    if num % 15 == 0 :
        ans.append("FizzBuzz")
    elif num % 3 == 0 :
        ans.append("Fizz")
    elif num % 5 == 0 :
        ans.append("Buzz")
    else :
        ans.append(num)
print(ans)