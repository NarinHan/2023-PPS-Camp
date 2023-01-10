'''
    A041 JadenCase 문자열 만들기
    JadenCase 란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열이다.
    문자열 s 가 주어졌을 때, s 를 JadenCase 로 바꾼 문자열을 리턴하는 프로그램을 작성하시오.
    https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''

s = input()
word = s.split()

changed = []
for w in word :
    temp = ""
    if w[0].isalpha :
        temp += w[0].upper()
        temp += w[1:].lower()
    else :
        temp += w[0]
        temp += w[1:].lower()
    changed.append(temp)

ans = " ".join(changed)
print(ans)