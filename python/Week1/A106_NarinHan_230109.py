'''
    A106 등장하지 않는 문자의 합
    주어진 문자열에서 등장하지 않는 알파벳 대문자의 아스키 코드 값의 합을 구하는 프로그램을 작성하시오.
    참고 : A = 65, Z = 90
'''

import string
alpha = string.ascii_uppercase # str type

num = int(input())
ans = [0] * num

for i in range(num) :
    temp = input()
    for ch in alpha :
        if ch not in temp :
            ans[i] += ord(ch)

for i in range(num) :
    print(ans[i])