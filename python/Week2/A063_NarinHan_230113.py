'''
    A063 Add Binary
    Given two binary strings a and b, return their sum as a binary string.
    e.g. a = 11, b = 1 -> a + b = 100
    https://leetcode.com/problems/add-binary/
'''
a = input()
b = input()

# 입력받은 a, b 를 한 자리씩 리스트에 저장
alist, blist = [], []
for ch in a :
    alist.append(int(ch))
for ch in b :
    blist.append(int(ch))

# 일의 자리부터 덧셈해야 하므로 reverse() 를 써서 리스트 뒤집기
alist.reverse()
blist.reverse()

# 자릿수가 더 작은 곳에 0 을 넣어 자릿수 맞추기
alen, blen = len(alist), len(blist)
if alen > blen :
    for i in range(alen - blen) :
        blist.append(0)
elif alen < blen :
    for i in range(blen - alen) :
        alist.append(0)

aidx, bidx, carry, anslist = 0, 0, 0, []
while True :
    # 모든 자릿수에 대해 계산이 끝난 경우
    if aidx == max(alen, blen) :
        if carry == 1 : # carry 가 1이면 리스트에 carry 를 추가
            anslist.append(carry)
        break
    
    ans = alist[aidx] + blist[bidx] + carry
    if ans == 3 :
        carry = 1
        anslist.append(1)
    elif ans == 2 :
        carry = 1
        anslist.append(0)
    elif ans == 1 :
        carry = 0
        anslist.append(1)
    elif ans == 0 :
        carry = 0
        anslist.append(0)
    aidx += 1
    bidx += 1

anslist.reverse()
for i in range(len(anslist)) :
    anslist[i] = str(anslist[i])
print("".join(anslist))