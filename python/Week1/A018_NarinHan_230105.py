'''
    A018 보물
    길이가 N 인 정수 배열 A 와 B 가 있다.
    함수 S = A[0] * B[0] + ... + A[N-1] * B[N-1] 이다.
    S 의 값을 가장 작게 만들기 위해 A 의 수를 재배열하고 (B 의 수는 재배열하면 안 됨) S 의 최솟값을 출력하라.
'''

num = int(input())
a = list(map(int, input().split())) # 리스트 요소들을 map 함수를 사용해 int 로 변환한 후, list 로 변환
b = list(map(int, input().split())) # 리스트 요소들을 map 함수를 사용해 int 로 변환한 후, list 로 변환
temp_b = b

a.sort() # a 를 오름차순으로 정렬
temp_b.sort(reverse=True) # b 를 내림차순으로 정렬

ans = 0
for i in range(num) :
    ans += a[i] * temp_b[i]

print(ans)