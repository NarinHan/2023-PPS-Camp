'''
    A075 가장 큰 수
    0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내주세요.
    https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''

nums = input().split(",") # 각 숫자를 문자열 타입의 리스트로 저장
nums.sort(reverse=True) # 아스키코드 값을 이용해 내림차순으로 정렬
ans = "".join(nums)
print(ans)