'''
    A053 스택
    정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
    - push X : 정수 X 를 스택에 넣음
    - pop : 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력, 스택에 들어있는 정수가 없는 경우 -1 출력
    - size : 스택에 들어있는 정수의 개수 출력
    - empty : 스택이 비어 있으면 1, 아니면 0 출력
    - top : 스택의 가장 위에 있는 정수 출력, 스택에 들어있는 정수가 없는 경우 -1 출력
'''

import sys # input() 을 쓰면 백준에서 시간초과가 떠서 sys.stdin.readline() 사용

num = int(sys.stdin.readline())

stack = []
for i in range(num) :
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push" :
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif cmd[0] == "size" :
        print(len(stack))
    elif cmd[0] == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif cmd[0] == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[len(stack)-1])