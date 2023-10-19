#include <iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    stack<char> st;
    for (int i = 0; i < s.size(); i++){
        if (st.size() > 0 && st.top() == s[i]){
            st.pop();
        }
        else{
            st.push(s[i]);
        }
    }
    
    if (st.size() == 0){
        return 1;
    }
    else{
        return 0;
    }
}