/*
    A007 음계 판별하기
    다장조 c d e f g a b C 8개 음을 각각 1-8 의 숫자로 바꾸어 표현
    연주한 순서가 주어졌을 때, 이것이 ascending, descending, mixed 중 무엇인지 판별
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// a > b 결과 반환하는 함수
bool desc(int a, int b) {
    return a > b;
}

int main() {

    vector<int> v, v_asc, v_desc;
    int temp;
    bool chk_asc = true, chk_desc = true;

    for(int i = 0; i < 8; i++) {
        cin >> temp;
        v.push_back(temp);
    }
    
    for(int i = 1; i <= 8; i++) {
        v_asc.push_back(i);
        v_desc.push_back(i);
    }

    sort(v_desc.begin(), v_desc.end(), desc);

    if(v == v_asc) {
        cout << "ascending" << endl;
    }
    else if(v == v_desc) {
        cout << "descending" << endl;
    }
    else {
        cout << "mixed" << endl;
    }

    return 0;
}