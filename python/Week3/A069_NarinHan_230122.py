'''
    A069 요세푸스 문제 0
    1 번부터 N 번까지 N 명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
    이제 순서대로 K 번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
    이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
    e.g. (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4> 이다.
    N 과 K 가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
    https://www.acmicpc.net/problem/11866
'''

n, k = map(int, input().split())
circle = [i+1 for i in range(n)]
cnt, ans = 0, list()
for i in range(n) :
    cnt += k-1
    if cnt >= len(circle) :
        cnt = cnt % len(circle)
    ans.append(circle.pop(cnt))
print(ans)
        