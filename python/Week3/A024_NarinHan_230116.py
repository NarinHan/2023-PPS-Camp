'''
    A024 Lemonade Change
    A lemonade costs $5 and customers are stading in a queue to buy the lemonades.
    Each customer will only buy one lemonade and pay with either a $5, $10, or $20.
    You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
    Return true if you can provide every customer with the correct change, or false otherwise.
    https://leetcode.com/problems/lemonade-change/
'''

bills = list(map(int, input().split(",")))
changes = list()
flag = 0
for b in bills :
    if b == 5 :
        changes.append(5)
    elif b == 10 :
        if 5 not in changes :
            flag = 1
            break
        elif 5 in changes :
            changes.remove(5)
            changes.append(10)
    elif b == 20 :
        if 10 and 5 not in changes :
            flag = 1
            break
        else :
            changes.remove(5)
            changes.remove(10)
            changes.append(20)

if flag == 0 :
    print(True)
else :
    print(False)