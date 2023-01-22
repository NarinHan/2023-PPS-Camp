'''
    A070 카드 2
    N 장의 카드가 있다. 각각의 카드는 차례로 1 부터 N 까지의 번호가 붙어 있으며, 1 번 카드가 제일 위에, N 번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
    이제 카드가 한 장 남을 때까지 다음을 반복한다. 우선 제일 위에 있는 카드를 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    e.g. N = 4 일 때 : 제일 위에서부터 1, 2, 3, 4 순서로 놓여있음 -> 1을 버리면 2, 3, 4 가 남음 -> 2를 제일 아래로 옮기면 3, 4, 2 가 됨 -> 반복하면 남는 카드는 4
    마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오. 
    https://www.acmicpc.net/problem/2164
'''

from collections import deque
n = int(input())
deq = deque([i+1 for i in range(n)])
while len(deq) != 1 :
    deq.popleft()
    deq.append(deq[0])
    deq.popleft()
print(deq[0])

# 시간초과를 해결하기 위해 검색하다가 찾은 라이브러리 사용!