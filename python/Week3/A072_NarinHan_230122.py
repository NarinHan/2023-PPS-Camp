'''
    A072 Day of the Year
    Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
    https://leetcode.com/problems/day-of-the-year/
'''

from datetime import datetime

date = input()
dateDT = datetime.strptime(date, "%Y-%m-%d") # 문자열을 datetime 으로 변환하는 strptime 메소드
first = date[:4] + "-1-1"
firstDT = datetime.strptime(first, "%Y-%m-%d")
diff = dateDT - firstDT # 두 날짜의 차이를 계산
print(diff.days + 1)

# datetime 을 문자열로 변환하는 메소드는 strftime