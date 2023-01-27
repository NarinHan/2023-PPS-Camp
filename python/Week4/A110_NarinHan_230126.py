'''
    A110 거스름돈
    JOI 잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 
    타로가 JOI 잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
'''

toPay = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
while toPay != 0 :
    for yen in money :
        cnt += toPay // yen
        toPay %= yen
print(cnt)
        