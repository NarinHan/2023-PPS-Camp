'''
    A046 농구 경기
    성(last name)의 첫 글자가 같은 선수가 5명이면 선발해서 경기를 진행하고, 그렇지 않으면 기권하려고 함
    선발할 수 있는 경우 가능한 성의 첫 글자를 사전순으로 공백없이 모두 출력, 기권해야 한다면 PREDAJA 출력
'''

num = int(input())
athelete = [] # 선수 이름 리스트
unique_lastname = dict() # key = 성의 첫 글자, value = 카운트 값
for i in range(num) :
    temp = input()
    athelete.append(temp)
    if temp[0] not in unique_lastname :
        unique_lastname[temp[0]] = 0

for p in athelete :
    unique_lastname[p[0]] += 1 # 선수들 last name 의 첫 글자 카운트

ans = []
for k, v in unique_lastname.items() :
    if v >= 5 : # 카운트한 값이 5 이상이면
        ans.append(k) # ans 리스트에 key 값 추가

if not ans : # ans 리스트가 비어 있다면
    anstr = "PREDAJA" # 기권 메시지 "PREDAJA"
else :
    ans.sort() # ans 리스트를 오름차순(사전순)으로 정렬
    anstr = ''.join(ans) # 정렬한 리스트를 문자열로 생성

print(anstr)

