'''
    A035 화성 수학
    화성에서 사용하는 수학 식은 지구의 것과 다르다 - @ : 3을 곱함, % : 5를 더함, # 7을 뺌
    화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음 연산자가 있음
'''

num = int(input())

def isNumber(s) :
    try :
        float(s)
        return True
    except ValueError :
        return False

ans = []
for i in range(num) :
    temp = input().split()
    for j in temp :
        if isNumber(j) :
            n = float(j)
        else :
            if j == "@" :
                n *= 3
            elif j == "%" :
                n += 5
            elif j == "#" :
                n -= 7
    ans.append(n)

for i in range(num) :
    print("%0.2f" % ans[i])