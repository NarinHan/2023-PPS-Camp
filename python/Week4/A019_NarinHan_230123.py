'''
    A019 숫자의 개수
    세 개의 자연수 A, B, C가 주어질 때 A * B * C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
    e.g. A = 150, B = 266, C = 427 이라면 A * B * C = 150 * 266 * 427 = 17037300 이 되고, 
    계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
'''

a, b, c = int(input()), int(input()), int(input())
mul = str(a * b * c)
num = [i for i in range(10)]
cnt = [0 for _ in range(10)]
for m in mul :
    for n in num :
        if int(m) == n :
            cnt[n] += 1
for c in cnt :
    print(c)