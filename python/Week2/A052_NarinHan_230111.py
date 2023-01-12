'''
    A052 OX 퀴즈
    OX 퀴즈의 결과가 주어지면 점수를 구하는 프로그램을 작성하시오.
    문제를 맞힌 경우, 그 문제의 점수는 그 문제까지 연속된 O 의 개수이다.
    예 : OOXXOXXOOO -> 1+2+0+0+1+0+0+1+2+3 = 10 점
    https://www.acmicpc.net/problem/8958
'''

num = int(input())
ans_list = [0] * num

for i in range(num) :
    temp = input()
    # O, X 를 한 글자씩 나누어 리스트에 저장
    temp_list = []
    for t in temp :
        temp_list.append(t)
    # 변수와 값 설정, for 문 돌면서 initialize 되도록 이곳에 설정함
    flag = -1 # flag 가 -1 이면 첫 글자, 0 이면 X, 1 이면 O
    cnt = 0
    ans = 0
    # 점수 계산
    for ch in temp_list :
        if ch == 'O' :
            if flag == -1 or flag == 0 :
                flag = 1
                cnt += 1
                ans += cnt
            elif flag == 1 :
                cnt += 1
                ans += cnt
        elif ch == 'X' :
            flag = 0
            cnt = 0
    ans_list[i] = ans

for a in ans_list :
    print(a)