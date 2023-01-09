/*
    A082 나이순 정렬
    온라인 저지에 가입한 사람들의 나이를 오름차순으로 정렬하라.
    나이가 같으면 먼저 가입한 사람이 앞에 오도록 정렬하라.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int,string> a, pair<int,string> b) {
    return a.first < b.first;
}

int main() {

    int num;
    vector<pair<int, string> > v;

    cin >> num;

    int age;
    string name;

    for(int i = 0; i < num; i++) {
        cin >> age;
        cin >> name;
        v.push_back(make_pair(age, name));
    }

    stable_sort(v.begin(), v.end(), compare); // 원래의 순서를 손상시키지 않으면서 sorting 하는 함수 

    for(int i = 0; i < v.size(); i++) {
        cout << v[i].first << " " << v[i].second << "\n";
    }

    return 0;
}