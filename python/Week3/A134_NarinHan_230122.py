'''
    A134 Reverse Prefix of Word
    Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 
    and ends at the index of the first occurrence of ch (inclusive). 
    If the character ch does not exist in word, do nothing.
    e.g. word = 'abcdefd', ch = 'd' -> result = 'dcbaefd' : first occurence of 'd' is at index 3, so reverse the from 0 to 3
'''

word = input()
ch = input()

if ch not in word :
    ans = word
else :
    idx = word.find(ch) # ch 가 처음으로 발견되는 index 저장
    temp1 = word[:idx+1] # index 0 부터 위에서 찾은 index 까지의 문자열 저장
    temp1 = temp1[::-1] # 찾은 문자열을 역순으로 재배치
    temp2 = word[idx+1:] # 역순 재배열이 필요없는 나머지 문자열 저장
    ans = temp1 + temp2
    
print(ans)

# 리스트를 쓰지 않고 슬라이싱으로 구해봤음! 