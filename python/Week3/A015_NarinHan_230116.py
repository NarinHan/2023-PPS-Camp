'''
    A015 검증수
    컴퓨터 제조 회사에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다.
    고유번호의 처음 5자리에는 00000 부터 99999 까지의 수 중 하나가 주어지며, 6번째 자리에는 검증수가 들어간다.
    검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지다.
    검증수를 출력하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/2475
'''

import sys

nums = list(map(int, sys.stdin.readline().split()))
temp = 0
for n in nums :
    temp += (n * n)
print(temp % 10)
