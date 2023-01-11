'''
    A049 비밀번호 발음하기
    발음이 가능한 비밀번호를 만들어 외우기 쉬우면서도 안전한 비밀번호 생성기를 만들자.
    - 모음(a, e, i, o, u) 하나를 반드시 포함한다.
    - 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    - 같은 글자가 연속적으로 두 번 오면 안되지만, ee 와 oo 는 허용한다.
    https://www.acmicpc.net/problem/4659
'''
import string

def listAlphabet() :
    return list(string.ascii_lowercase)

vw_list = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트
dvw_list = ['aa', 'ii', 'uu'] # 더블 모음 리스트
# 자음 리스트 생성
cs_list = listAlphabet()
for vw in vw_list :
    cs_list.remove(vw)
# 더블 자음 리스트 생성
dcs_list = []
for cs in cs_list :
    dcs_list.append(cs * 2)

pw_list = []
while True :
    temp = input()
    if temp == "end" : # end 가 나올 때까지 단어를 입력받음
        break
    pw_list.append(temp) # 입력받은 단어 목록을 리스트에 저장

# 입력받은 비밀번호와 acceptable/unacceptable 을 함께 저장할 딕셔너리 생성
pw_dict = {}
for pw in pw_list :
    pw_dict[pw] = "acceptable" # 초기엔 모두 acceptable 로 설정

for pw in pw_list :
    # 1번 조건 : 단어에 모음이 포함되어 있지 않으면 unacceptable
    if not any(vw in pw for vw in vw_list) : # any() : 하나라도 True 인 게 있으면 True 반환
        pw_dict[pw] = "not acceptable"
    # 3번 조건 : 같은 글자가 연속으로 2번 오면 unacceptable
    elif any(dvw in pw for dvw in dvw_list) :
        pw_dict[pw] = "not acceptable"
    elif any(dcs in pw for dcs in dcs_list) :
        pw_dict[pw] = "not acceptable"
    else :
        # 2번 조건 : 모음이 3개 또는 자음이 3개 연속으로 나오면 unacceptable
        vwCnt = 0
        csCnt = 0
        flag = -1
        for ch in pw :
            if ch in vw_list :
                if flag == -1 : # 단어의 첫 글자라면
                    flag = 0 # flag 를 모음으로 바꿔주고
                    vwCnt += 1 # 모음 카운트 올리기
                elif flag == 0 : # flag 가 모음이면
                    vwCnt += 1 # 모음 카운트 올리기
                    if vwCnt >= 3 : # 연속된 모음이 3개 이상이면 not acceptable
                        pw_dict[pw] = "not acceptable"
                        break
                elif flag == 1 : # flag 가 자음이면
                    flag = 0 # flag 를 모음으로 바꿔주고
                    csCnt = 0 # 자음 카운트 리셋
                    vwCnt += 1 # 모음 카운트 올리기
            elif ch in cs_list :
                if flag == -1 :
                    flag = 1
                    csCnt += 1
                elif flag == 0 :
                    flag = 1
                    vwCnt = 0
                    csCnt += 1
                elif flag == 1 :
                    csCnt += 1
                    if csCnt >= 3 :
                        pw_dict[pw] = "not acceptable"
                        break

for pw in pw_dict :
    print("<{}> is {}.".format(pw, pw_dict[pw]))