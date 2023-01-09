/*
    A077 점수 계산
    8개 문제 중 가장 높은 점수 5개의 합으로 최종 점수를 구한다.
    총 점수를 구하는 프로그램을 작성하시오.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    return a.first > b.first;
}

bool idxCompare(pair<int, int> a, pair<int, int> b) {
    return a.second < b.second;
}

int main() {

    int temp, sum = 0;
    vector<pair<int, int> > v;

    for(int i = 0; i < 8; i++) {
        cin >> temp;
        v.push_back(make_pair(temp, i+1));
    }

    sort(v.begin(), v.end(), compare);
    for(int i = 0; i < 5; i++) {
        sum += v[i].first;
    }
    
    cout << sum << endl;
    for(int i = 0; i < 5; i++) {
        sort(v.begin(), v.begin()+5, idxCompare);
        cout << v[i].second << " ";
    }

    return 0;
}