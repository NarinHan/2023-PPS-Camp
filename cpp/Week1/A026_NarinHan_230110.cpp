/*
    A026 하샤드 수
    양의 정수 x 가 하샤드 수이려면 x 의 자릿수의 합으로 x 가 나누어져야 한다.
    예 : 18 의 자릿수 합 = 1 + 8 = 9 -> 18 은 9로 나누어 떨어지므로 18은 하샤드 수
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

    int num, digit = 0, temp;
    bool ans = true;

    cin >> num;
    temp = num;

    while(temp >= 1) {
        digit += temp % 10;
        temp /= 10;
    }

    if(num % digit == 0) {
        ans = true;
    }
    else {
        ans = false;
    }

    cout << ans;

    return 0;
}