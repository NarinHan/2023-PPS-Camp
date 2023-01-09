'''
    A094 크로아티아 알파벳
    단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력하라.
    https://www.acmicpc.net/problem/2941
'''

word = input()

alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for ch in alphabet_list :
    word = word.replace(ch, "*")

print(len(word))