'''
    A128 균형잡힌 세상
    어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜시오.
    문자열에 포함되는 괄호는 소괄호()와 대괄호[]로 2 종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
    - 모든 왼쪽 소괄호는 오른쪽 소괄호와 짝을 이뤄야 한다.
    - 모든 왼쪽 대괄호는 오른쪽 대괄호와 짝을 이뤄야 한다.
    - 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
    - 모든 괄호들의 짝은 1:1 매칭만 가능하다.
    - 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
    https://www.acmicpc.net/problem/4949
'''

import sys
while True :
    temp = sys.stdin.readline().rstrip()
    stack = list()
    flag = 0 # 그 줄의 괄호가 다 맞았는지 체크
    if temp == '.' :
        break
    for t in temp :
        if t == '(' or  t == '[' : # 왼쪽 괄호면 스택에 푸쉬
            stack.append(t)
        elif t == ')' : # 오른쪽 소괄호일 때
            if not stack or stack[-1] == '[' : # 스택이 비어있거나 스택에 있는 것이 오른쪽 대괄호면 no
                print("no")
                flag = 1
                break
            else : # 짝이 맞으면 스택의 ( 제거
                stack.pop() 
        elif t == ']' : # 왼쪽 대괄호일 때
            if not stack or stack[-1] == '(' : # 스택이 비어있거나 스택에 있는 것이 오른쪽 소괄호면 no
                print("no")
                flag = 1
                break
            else :
                stack.pop() # 짝이 맞으면 스택의 [ 제거
    if flag == 0 : # no 가 하나도 없을 때
        if not stack : # 스택이 비어있다면
            print("yes")
        else :
            print("no")


