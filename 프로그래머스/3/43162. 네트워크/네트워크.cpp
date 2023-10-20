#include <string>
#include <vector>
#include <iostream>
#include <deque>

using namespace std;
vector<bool> visited;

void bfs(vector<vector<int>> computers, int start){
    deque<int> dq;
    dq.push_back(start);
    
    while (!dq.empty()){
        int curr = dq.front();
        dq.pop_front();
        vector<int> connected = computers[curr];
        for (int c = 0; c < connected.size(); c++){
            if (connected[c] == 1 && !visited[c]){
                dq.push_back(c);
                visited[c] = true;
            }
        }
        
    }
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++){
        visited.push_back(false);
    }
    
    for (int c = 0; c < n; c++){
        if (!visited[c]){
            visited[c] = true;
            bfs(computers, c);
            answer ++;
        }
    }
    
    return answer;
}