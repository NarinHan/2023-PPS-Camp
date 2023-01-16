'''
    A066 소트인사이드
    배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
    https://www.acmicpc.net/problem/1427
'''
import sys
num = sys.stdin.readline()
numList = [n for n in num]
numList.sort(reverse=True)
print("".join(numList))