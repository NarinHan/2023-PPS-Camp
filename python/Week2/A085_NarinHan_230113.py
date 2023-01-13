'''
    A085 시리얼 번호
    다솜이는 기타를 시리얼 번호 순서대로 정렬하고자 한다. 모든 시리얼 번호는 알파벳 대문자와 숫자로 이루어져 있다.
    시리얼 번호 A 가 시리얼 번호 B 의 앞에 오는 경우는 다음과 같다.
    - A 와 B 의 길이가 다르면, 짧은 것이 먼저 온다
    - 서로 길이가 같다면, A 의 모든 자릿수의 합과 B 의 모든 자릿수의 합을 비교해서 작은 합을 가지는 것이 먼저온다 (숫자만 더한다)
    - 위 두 조건으로도 비교할 수 없으면, 사전순으로 비교한다; 숫자가 알파벳보다 사전순으로 작다
    https://www.acmicpc.net/problem/1431
'''

import sys

num = int(sys.stdin.readline())

guitar = list()
for i in range(num) :
    temp = sys.stdin.readline().strip()
    sum = 0
    # 입력받을 때 각 자릿수를 모두 더해서 [입력받은 값, 자릿수 합] 형태의 리스트로 저장
    for t in temp :
        if t.isdigit() :
            sum += int(t)
    guitar.append((temp, sum))

# 조건 순서대로 정렬 - 1) 길이 2) 자릿수 합 3) 사전순
guitar.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for g in guitar :
    print(g[0])