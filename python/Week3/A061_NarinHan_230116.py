'''
    A061 Excel Sheet Column Title
    Given an integer column number, return its corresponding column title as it appears in an Excel sheet.
    e.g. A : 1, B : 2, ..., Z : 26, AA : 27, AB : 28
    https://leetcode.com/problems/excel-sheet-column-title/
'''

import string

colNum = int(input())
num = [i for i in range(1, 27)] # 1-26 리스트 생성
alpha = [i for i in string.ascii_uppercase] # 대문자 리스트 생성
d = dict(zip(num, alpha)) # key=숫자, value=대문자 딕셔너리 생성
d[0] = "" # 딕셔너리 마지막에 {0 : 공백} 추가
ans = ""
while colNum > 0 :
    r = colNum % 26
    ans += d[r]
    colNum //= 26
    if colNum > 26 :
        continue
    else :
        ans += d[colNum]
        break
print(ans[::-1]) # 끝자리부터 구했으므로 뒤집어서 출력