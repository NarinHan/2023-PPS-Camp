'''
    A032 부녀회장이 될테야
    평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
    이 아파트의 거주 조건은 "a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다" 이다.
    아파트에 비어있는 집이 없고, 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 
    주어지는 양의 정수 k와 n에 대해 k층 n호에는 몇 명이 살고 있는지 출력하라. 
    단, 아파트는 0층부터 있고 각층은 1호부터 있으며, 0층의 i호에는 i명이 산다.
    https://www.acmicpc.net/problem/2775
'''

num = int(input())
for i in range(num) :
    floor = int(input())
    house = int(input())
    apt = [j+1 for j in range(house)] # 아파트 0층
    for f in range(floor) :
        for h in range(1, house) :
            apt[h] += apt[h-1]
    print(apt[-1])


# 매트릭스의 누적 합이니 전체 매트릭스를 구하려고 했는데, 계산하면 행의 값이 전부 똑같이 바뀜... shallow copy, deep copy 문제인가?
