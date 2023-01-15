'''
    A119 Guess Number Higher or Lower
    I pick a number from 1 to n and you have to guess which number I picked.
    Every time you guess worng, I will tell you whether the number I picked is higher or lower than your guess.
    - Results : -1 if num > pick, 1 if num < pick, 0 if num == pick
    Return the number that I picked.
    https://leetcode.com/problems/guess-number-higher-or-lower/
'''

n = int(input())
pick = int(input())

import random

while True :
    guess = random.randrange(1, n+1) # randomly guessed number
    if guess > pick :
        flag = -1
    elif guess < pick :
        flag = 1
    else :
        flag = 0

    if flag == -1 :
        guess = random.randrange(1, guess)
    elif flag == 1 :
        guess = random.randrange(guess, n+1)
    else :
        break

print(guess)