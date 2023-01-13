'''
    A064 Height Checker
    Students are asked to stand in a single file line in non-decreasing order by height.
    Let this ordering be represented by the integer array expected where expected[i] is the expected height of the i-th student in line.
    Return the number of indices where heights[i] != expected[i]
    https://leetcode.com/problems/height-checker/
'''

ori = list(map(int, input().split(",")))
expected = ori.copy()
expected.sort()

ans = 0
for i in range(len(ori)) :
    if ori[i] != expected[i] :
        ans += 1

print(ans)

# ori 와 expected 로 dictionary 를 만들어서 key, value 로 간편하게 출력하려 했는데
# dictionary 는 key 값의 중복을 허용하지 않는다는 놀라운(?) 사실을 알게 됨!
# (+) 두 개의 리스트를 dictionary 로 묶으려면 zip(list1, list2) 쓰면 편하게 됨!