/*
    A042 Backspace String Compare
    Given two strings s and t, return true if they are equal when both are typed into empty text editors.
    '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.
    https://leetcode.com/problems/backspace-string-compare/
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {

    string s, t;

    cin >> s;
    cin >> t;

    stack<char> ss;
    stack<char> ts;

    for(int i = 0; i < s.length(); i++) {
        ss.push(s[i]);
        if(s[i] == '#') {
            ss.pop();
            ss.pop();
        }
    }

    for(int i = 0; i < t.length(); i++) {
        ts.push(t[i]);
        if(t[i] == '#') {
            ts.pop();
            ts.pop();
        }
    }
    
    string sans = "", tans = "";
    for(int i = 0; i < ss.size(); i++) {
        sans += ss.top();
        ss.pop();
    }

    for(int i = 0; i < ts.size(); i++) {
        tans += ts.top();
        ts.pop();
    }

    if(sans == tans) {
        cout << "true" << endl;
    }
    else {
        cout << "false" << endl;
    }


    return 0;
}