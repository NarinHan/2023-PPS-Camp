'''
    A104 욱제는 효도쟁이야
    각 마을에서 마을까지의 이동 비용이 주어질 때, 욱제가 최소한의 이동비용으로 부모님을 모시고 섬의 모든 마을을 관광하려면 얼마의 이동 비용이 드는지 구하라.
    임의의 A 마을에서 임의의 B 마을로 가기 위해서는 왼쪽 또는 오른쪽 도로를 통해 해안가를 따라 섬을 돌아야 한다.
'''

num = input()
cost = list(map(int, input().split()))
cost.sort()
sum = 0
for i in range(int(num)-1) :
    sum += cost[i]
print(sum)