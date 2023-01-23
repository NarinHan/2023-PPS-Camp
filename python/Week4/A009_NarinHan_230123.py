'''
    A009 문자열 다루기 기본
    문자열 's'의 길이가 4 혹은 6 이고, 숫자로만 구성돼있는지 확인하는 프로그램을 작성하세요.
    e.g. a234 -> False, 1234 -> True
    https://school.programmers.co.kr/learn/courses/30/lessons/12918
'''

s = input()
if (len(s) == 4 or len(s) == 6) :
    if s.isalpha() or s.isdigit() :
        print(True)
    else :
        print(False)
else :
    print(False)