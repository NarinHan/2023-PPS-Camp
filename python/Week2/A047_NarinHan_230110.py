'''
    A047 열 개씩 끊어 출력하기
    알파벳 소문자와 대문자로만 이루어진 길이가 n 인 단어가 주어진다.
    한 글에 10 글자씩 끊어서 출력하는 프로그램을 작성하시오.
'''

s = input()

i = 10
while True :
    print(s[i-10:i])
    i += 10
    if(i >= len(s)) :
        print(s[i-10:])
        break