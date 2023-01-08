'''
    A084 접미사 배열
    문자열 S 의 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
    예 : baekjoon 의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있음
'''

word = input()
suffix_list = []
for i in range(len(word)) :
    suffix = word[i:]
    suffix_list.append(suffix)

suffix_list.sort()
for suffix in suffix_list :
    print(suffix)