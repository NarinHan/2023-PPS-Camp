'''
    A023 Add Digits
    Given an integer number, repeatedly add all its digits until the result has only one digit and return it.
    e.g. num = 38 -> 3 + 8 = 11 -> 1 + 1 = 2
'''

num = input()

temp = 0
while True :
    for i in num :
        temp += int(i)
    if len(str(temp)) == 1 :
        ans = temp
        break
    else :
        num = str(temp)
        temp = 0

print(ans)