'''
    A050 카이사르 암호
    카이사르는 편지를 쓸 때 알파벳 문자를 3개씩 건너뛰어 적었다.
    예를 들어 'A'를 'D'로, 'B'를 'E'로, 'C'를 'F'로 적은 것이다.
    카이사르 암호 형식으로 얻은 문자를 원래대로 돌려놓는 프로그램을 작성하시오.
'''

word = input()
ans = ""
for ch in word :
    if ch == 'A' :
        ans += 'X'
    elif ch == 'B' :
        ans += 'Y'
    elif ch == 'C' :
        ans += 'Z'
    else :
        ans += chr(ord(ch) - 3)
print(ans)