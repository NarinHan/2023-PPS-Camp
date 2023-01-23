'''
    A060 Baseball Game
    You are keeping the scores for a baseball game with strange rules.
    At the beginning of the game, you start with an empty record.
    You are given a list of strings 'operations',
    where operations[i] is the i-th operation you must apply to the record and is one of the following :
    - An integer x : record a new score of x
    - '+' : record a new score that is the sum of the previous two scores
    - 'D' : record a new score that is the double of the previous score
    - 'C' : invalidate the previous score, removing it from the record
    Return the sum of all the scores on the record after applying all the operations
    https://leetcode.com/problems/baseball-game/
'''

ops = input().split(",")
res = list()
for op in ops :
    if op == 'D' :
        res.append(res[-1] * 2)
    elif op == 'C' :
        res.pop()
    elif op == "+" :
        res.append(res[-1] + res[-2])
    else :
        res.append(int(op)) # 숫자면 res 리스트에 int type 으로 추가
print(sum(res))