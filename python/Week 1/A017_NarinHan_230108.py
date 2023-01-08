'''
    A017 방 번호
    다솜이의 방 번호가 주어졌을 때, 필요한 0-9 까지의 숫자 세트 개수의 최솟값을 구하시오.
    6 과 9 는 서로 뒤집어서 사용할 수 있다.
'''

num = input()
cnt = [0] * 9
for x in num :
    idx = int(x)
    if idx == 9 :
        idx = 6
    cnt[idx] += 1
cnt[6] = (cnt[6] + 1) // 2
print(max(cnt))