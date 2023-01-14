'''
    A037 Self Dividng Numbers
    Find self-dividing number which is a number that is divisible by every digit it contains
    e.g. 128 -> 128 % 1 == 0, 128 % 2 == 0, 128 % 8 == 0
    Given left and right, return a list of all the self-dividng numbers in the range [left, right]
'''

left = int(input())
right = int(input())

num = []
for i in range(left, right + 1) :
    num.append(str(i))

flag = True
exclude = []
for i in range(len(num)) :
    for j in num[i] :
        if int(j) == 0 :
            flag = False
        elif int(num[i]) % int(j) != 0 :
            flag = False
        else :
            flag = True
        if flag == False :
            exclude.append(num[i])

ans = num
for i in exclude :
    if i in num :
        ans.remove(i)

print(ans)