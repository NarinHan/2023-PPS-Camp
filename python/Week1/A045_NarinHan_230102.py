'''
    A045 단어 공부
    알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 찾으시오, 대소문자 구별하지 않음
    가장 많이 사용된 알파벳을 대문자로 출력, 여러 개 존재하는 경우 "?" 출력
'''

temp = input().upper() # 문자열 입력받은 후 전체 대문자로 전환
unique_list = list(set(temp)) # 중복 제거 후 각 문자를 리스트에 저장 

cnt_list = []
for ch in unique_list :
    n = temp.count(ch) # 입력받은 문자에 들어있는 각 문자의 개수 카운트해서
    cnt_list.append(n) # cnt_list 에 카운트한 값을 추가

if cnt_list.count(max(cnt_list)) > 1 : # 가장 많이 사용된 알파벳의 값이 2개 이상인 경우 
    print("?")
else :
    max_idx = cnt_list.index(max(cnt_list)) # 가장 많이 사용된 알파벳의 인덱스 찾기
    print(unique_list[max_idx])