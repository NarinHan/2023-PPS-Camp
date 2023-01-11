'''
    A048 그룹 단어 체커
    그룹 단어란 단어에 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나는 경우만을 말한다.
    예 : ccazzzzbb -> c, a, z, b 가 모두 연속해서 나타나므로 그룹 단어, aabbbccb -> b 가 떨어져서 나타나기 때문에 그룹 단어가 아님
    https://www.acmicpc.net/problem/1316
'''

num = int(input())
ans = num
for i in range(num) :
    temp = input()
    for t in temp :
        tCnt = temp.count(t)
        find = t * tCnt
        if (tCnt >= 2) and (find not in temp) :
            ans -= 1
            break
        
print(ans)