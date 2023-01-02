/* 
    A006 문자열 내 p 와 y 의 개수
    대문자와 소문자가 섞여있는 문자열 s 에서 p 의 개수와 y 의 개수를 비교해 같으면 true, 다르면 false 를 return
    p 와 y 가 하나도 없는 경우 항상 true 를 return, 대소문자 구별하지 않음 
*/ 

#include <iostream>
#include <string>

using namespace std;

int main() {

    bool answer = true;
    string input, temp = "";
    int nump = 0, numy = 0;

    cin >> input;

    for(int i = 0; i < input.length(); i++) {
        temp += tolower(input[i]); 
    }

    for(int i = 0; i < temp.length(); i++) {
        if(temp[i] == 'p') {
            nump++;
        }
        else if(temp[i] == 'y') {
            numy++;
        }
    }

    if(nump != numy) {
        answer = false;
    }

    cout << answer;    

    return 0;
}