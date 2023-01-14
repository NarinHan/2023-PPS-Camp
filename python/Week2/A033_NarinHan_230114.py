'''
    A033 나는 요리사다
    다섯 참가자들이 요리 실력을 뽐내는 티비 프로그램 "나는 요리사다" 에서는 서로 다른 사람의 음식을 평가해준다.
    점수는 1점부터 5점까지 있으며, 각 참가자가 얻은 점수는 다른 사람이 평가해준 점수의 합이다.
    우승자는 가장 많은 점수를 얻은 사람이다. 우승자와 그의 점수를 구하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/2953
'''

sum = [list(map(int, input().split())) for i in range(5)]
maxt = 0
for i in range(5) :
    temp = 0
    for j in range(4) :
        temp += sum[i][j]
    sum[i].append(temp)
    if temp >= maxt :
        maxt = temp
        idx = i
print(idx + 1, maxt)