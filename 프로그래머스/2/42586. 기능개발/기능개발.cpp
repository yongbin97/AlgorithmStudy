#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int curr_time = 0;
    stack<int> st;
    
    
    for (int i = 0; i < progresses.size(); i++){
        // 현재 작업 걸리는 시간 계산
        int time = (100 - progresses[i]) / speeds[i];
        if ((100 - progresses[i]) % speeds[i] > 0){
            time ++;
        }
        
        // 현재 시간보다 더 걸림 -> stack에 있는 것 모두 뽑기
        if (curr_time < time){
            int count = 0;
            while (!st.empty() && st.top() <= curr_time){
                st.pop();
                count ++;
            }
            if (count > 0) answer.push_back(count);
            curr_time = time;
        }
        st.push(time);
        
    }
    answer.push_back(st.size());
    
    return answer;
}