'''
    B031 라디오
    최근 준하가 구입한 라디오는 매우 하이테크한데, 그 라디오에는 다음과 같은 버튼이 있다.
    - 첫 번째 버튼은 주파수를 1MHz 증가시킨다.
    - 두 번째 버튼은 주파수를 1MHz 감소시킨다.
    - 나머지 N개의 버튼은 즐겨찾기 기능으로, 미리 지정된 주파수로 이동한다.
    현재 주파수 A와 듣고싶은 주파수 B가 주어질 때, 주파수 A에서 B로 갈 때 눌러야 하는 가장 적은 버튼수를 구해주자.
    https://www.acmicpc.net/problem/3135
'''

a, b = map(int, input().split())
n = int(input())
fav, cnt = list(), 0
for i in range(n) :
    fav.append(int(input()))
temp = abs(a - b)
for f in fav :
    temp = min(temp, abs(f - b))
if temp == abs(a - b) :
    cnt = temp
else :
    cnt = temp + 1
print(cnt)
