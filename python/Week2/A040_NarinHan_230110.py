'''
    A040 Determine if String Halves Are Alike
    Given a string of even length, split this string into two halves of equal lengths.
    Determine if the first half and the second half are alike - have the same number of vowels.
    A string contains both lowercase and uppercase letters.
    e.g. book -> 'bo' and 'ok' -> each has one vowel -> alike
    https://leetcode.com/problems/determine-if-string-halves-are-alike/
'''

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

s = input()
ls = len(s) // 2

a = s[0:ls]
b = s[ls:]

aCnt = 0
bCnt = 0
for v in vowels :
    aCnt += a.count(v)
    bCnt += b.count(v)
    
if aCnt == bCnt :
    print(True)
else :
    print(False)