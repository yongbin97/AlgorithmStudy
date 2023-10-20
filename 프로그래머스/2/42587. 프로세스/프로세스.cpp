#include <string>
#include <vector>
#include <algorithm>
#include <deque>
#include <iostream>

using namespace std;


int solution(vector<int> priorities, int location) {
    deque<pair<int, int>> dq;
    
    for (int i = 0; i < priorities.size(); i++){
        dq.push_back({priorities[i], i});
    }
    pair<int, int> max = *max_element(dq.begin(), dq.end());
    
    int idx = 1;
    while (true){
        pair<int, int> curr = dq[0];
        dq.pop_front();
        
        if (curr.first == max.first){
            if (curr.second == location){
                return idx;
            }
            idx ++;
            max = *max_element(dq.begin(), dq.end());
        }
        else{
            dq.push_back(curr);
        }
    }
}