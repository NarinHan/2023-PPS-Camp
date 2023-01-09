'''
    A108 수 뒤집기
    원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.
    예 : 124 <-> 421 => 합 = 545 대칭
'''

num = int(input())
ans = []
for i in range(num) :
    temp = input()
    reversed_temp = temp[::-1]
    ans_temp = str(int(temp) + int(reversed_temp))
    if ans_temp == ans_temp[::-1] :
        ans.append("YES")
    else :
        ans.append("NO")
    
for i in range(num) :
    print(ans[i])