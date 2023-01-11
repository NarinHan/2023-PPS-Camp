'''
    A044 Student Attendance Record 1
    Given a string representing an attendance record for a student, determine if the student is eligible for an attendance award. 
    Each character signifies absent(A), late(L), present(P).
    The student is eligible for an attendance award if they meet both of the following criteria :
    - Absent for strictly fewer than 2 days total
    - Never late for 3 or more consecutive days
    https://leetcode.com/problems/student-attendance-record-i/
'''

s = input()

if s.count('A') >= 2 :
    ans = False
elif 'LLL' in s :
    ans = False
else :
    ans = True

print(ans)