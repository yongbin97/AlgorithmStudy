#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for(int s: scoville){
        pq.push(s);
    }
    while (pq.size() > 1 && pq.top() < K){
        int s_first = pq.top();
        pq.pop();
        int s_second = pq.top();
        pq.pop();
        
        pq.push(s_first + s_second * 2);
        answer ++;
    }
    if (pq.size() == 1 && pq.top() < K){
        return -1;
    }
    return answer;
}