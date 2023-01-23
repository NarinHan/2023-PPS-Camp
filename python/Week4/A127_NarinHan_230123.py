'''
    A127 최소공배수
    두 자연수 A 와 B 가 주어졌을 때, A 와 B 의 최소공배수를 구하는 프로그램을 작성하시오.
    첫째 줄에 테스트 케이스의 개수 T 가, 둘째 줄 부터 T 개의 줄에 걸쳐 A 와 B 가 주어진다.
    https://www.acmicpc.net/problem/1934
'''

import sys
num = int(sys.stdin.readline())
for i in range(num) :
    a, b = map(int, sys.stdin.readline().split())
    atemp, btemp = a, b
    while atemp != 0 :
        btemp = btemp % atemp
        atemp, btemp = btemp, atemp
    gcd = btemp
    lcm = a * b // btemp
    print(lcm)

