'''
    A021 플러그
    선영이 집에는 콘센트를 꽂을 수 있는 플러그가 하나밖에 없어서 N 개의 멀티탭을 사용한다.
    각 멀티탭은 몇 개의 플러그로 이루어져 있는데, 최대 몇 대의 컴퓨터를 연결할 수 있을까?
    https://www.acmicpc.net/problem/2010
'''

import sys

n = int(sys.stdin.readline().strip())
ans = 0
for i in range(n) :
    ans += int(sys.stdin.readline().strip()) - 1
print(ans + 1) # 마지막 멀티탭은 플러그를 모두 쓸 수 있으므로 +1