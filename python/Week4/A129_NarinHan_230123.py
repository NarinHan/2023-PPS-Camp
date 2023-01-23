'''
    A129 1,2,3 더하기
    정수 4 를 1, 2, 3 의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
    1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
    정수 n 이 주어졌을 때, n 을 1, 2, 3 의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/9095
'''

t = int(input())
for i in range(t) :
    n = int(input())
    dp = [0] * (n + 1)
    if n == 1 :
        print(1)
    elif n == 2 :
        print(2)
    elif n == 3 : 
        print(4)
    else :
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4, n+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])


# 점화식 : n > 3 일 때 f(n) = f(n-1) + f(n-2) + f(n-3)