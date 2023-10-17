#include<string>
#include<stack>
#include <iostream>

using namespace std;

bool solution(string s)
{
    stack<char> st;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '(') st.push('(');
        else{
            if (st.empty() || st.top() == ')') return false;
            st.pop();
        }
    }
    return st.empty();
}