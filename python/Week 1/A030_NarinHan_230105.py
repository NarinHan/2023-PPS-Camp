'''
    A030 좋은 날 싫은 날
    재현이는 매일이 기분이 좋은 날, 기분이 싫은 날 두 가지로 나누어지고, 오늘의 기분은 내일의 기분에 영향을 준다.
    N 일 뒤의 재현이의 기분이 어떨지 알려주는 프로그램을 만들어 보자.
    첫째 줄에 정수 N 과 현재 재현이의 기분(좋은 날 0, 싫은 날 1)이 주어지고, 둘째 줄에 P(G|G), P(B|G), P(G|B), P(B|B) 주어진다.
    예 : 2 1 \n 0.70 0.30 0.50 0.50
    ========================================================
    풀이
    - 2일 뒤 재현이의 기분이 좋을 확률 = P(G|B) * P(G|G) + P(B|B) + P(G|B) = 0.50 * 0.70 + 0.50 * 0.50 = 0.60
    - 2일 뒤 재현이의 기분이 나쁠 확률 = P(B|B) * P(B|B) + P(G|B) * P(B|G) = 0.50 * 0.50 + 0.50 * 0.30 = 0.40
'''

num, init = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

gCnt = [0.0 for i in range(num)]
bCnt = [0.0 for i in range(num)]

if init == 0 :
    gCnt[0] = gg
    bCnt[0] = gb
else :
    gCnt[0] = bg
    bCnt[0] = bb

for i in range(1, num) :
    gCnt[i] = gCnt[i-1] * gg + bCnt[i-1] * bg
    bCnt[i] = gCnt[i-1] * gb + bCnt[i-1] * bb

print(round(gCnt[num-1] * 1000))
print(round(bCnt[num-1] * 1000))