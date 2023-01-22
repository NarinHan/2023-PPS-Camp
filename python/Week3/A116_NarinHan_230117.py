'''
    A116 Day of the Week
    Given a date, return the corresponding day of the week for that date.
    The input is given as three integers representing the day, month and year respectively.
    https://leetcode.com/problems/day-of-the-week/
'''

day = int(input())
month = int(input())
year = int(input())

import datetime # datetime 모듈로 쉽게 날짜 계산 가능!

myweekday = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
temp = datetime.datetime(year, month, day).weekday()
print(myweekday[temp])