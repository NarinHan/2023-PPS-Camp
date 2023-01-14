/*
    A081 N 번째 큰 수
    배열 A 가 주어졌을 때, N 번째 큰 값을 출력하는 프로그램을 작성하시오.
    배열 A 의 크기는 항상 10이고, 자연수만 가지고 있으며, N 은 항상 3이다.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int num;
    int arr[10];
    vector<int> ans;

    cin >> num;
    for(int i = 0; i < num; i++) {
        for(int j = 0; j < 10; j++) {
            cin >> arr[j];
        }
        sort(arr, arr+10, greater<int>());
        ans.push_back(arr[2]);
    }

    for(int i = 0; i < num; i++) {
        cout << ans[i] << endl;
    }

    return 0;
}