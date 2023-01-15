'''
    A124 소인수분해
    정수 N 의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/11653
'''

n = int(input())
ans = list()
temp, flag = 2, n

while True :
    if n % temp == 0 :
        n = n // temp
        ans.append(temp)
        flag /= temp
        if flag == 1 :
            break
        temp = 2
    else :
        temp += 1

ans.sort()
for i in ans :
    print(i)