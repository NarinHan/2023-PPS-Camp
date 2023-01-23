'''
    A026 하샤드 수
    양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
    e.g. 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
    자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 프로그램을 완성해주세요.
    https://school.programmers.co.kr/learn/courses/30/lessons/12947
'''

num = input()
temp = 0
for n in num :
    temp += int(n)
if temp % 9 == 0 :
    print(True)
else :
    print(False)
