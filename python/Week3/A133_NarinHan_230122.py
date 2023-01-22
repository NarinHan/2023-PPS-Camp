'''
    A133 Capitalize the Title
    Given a 'title' consisting of one or more words separated by a single space, where each word consists of English letters,
    capitalize the string by changing the capitalization of each word such that :
    - If the length of the word is 1 or 2 letters, change all letters to lowercase
    - Otherwise, change the first letter to uppercase and the remaining letters to lowercase
    Return the capitalized 'title'.
    https://leetcode.com/problems/capitalize-the-title/
'''

title = input().split()
ans = ""
if len(title) <= 2 :
    ans = title[0].lower()
else :
    for t in title :
        ans += t.capitalize()
        ans += " "
print(ans)

# 피어 리뷰 진행하면서 알게된 capitalize() 메소드를 써봤음!