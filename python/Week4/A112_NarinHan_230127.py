'''
    A112 기타줄
    기타리스트 강토가 사용하는 기타에서 N 개의 줄이 끊어졌다.
    새로운 줄을 사거나 교체해야 하는데 되도록이면 돈을 적게 쓰려고 한다.
    6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
    끝어진 기타줄의 개수 N 과 기타줄 브랜드 M 개가 주어지고, 
    각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 
    적어도 N 개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/1049
'''

n, m = map(int, input().split())
if n % 6 != 0 :
    packNum = n // 6 + 1
    rem = n % 6
else :
    packNum = n // 6
    rem = 0
pack, single = list(), list()
for i in range(m) :
    p, s = map(int, input().split())
    pack.append(p)
    single.append(s)
mp = min(pack)
ms = min(single)
ans = min(mp * packNum, ms * n)
if rem != 0 :
    ans = min(ans, mp * (packNum-1) + rem * ms)
print(ans)
