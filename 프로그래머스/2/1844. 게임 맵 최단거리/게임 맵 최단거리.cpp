#include<vector>
#include<deque>
#include<iostream>

using namespace std;

pair<int, int> direction[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
vector<vector<int>> visited;

int solution(vector<vector<int>> maps)
{
    for (int i = 0; i < maps.size(); i++){
        vector<int> row;
        for (int j = 0; j < maps[0].size(); j++){
            row.push_back(0);
        }
        visited.push_back(row);
    }
    
    deque<pair<int, int>> dq;
    dq.push_back({0, 0});
    visited[0][0] = 1;
    while (!dq.empty()){
        pair<int, int> curr = dq.front();
        dq.pop_front();
        for (pair<int, int> d: direction){
            pair<int, int> next = {curr.first + d.first, curr.second + d.second};
            if (
                next.first >= 0 && next.first < maps.size()
                && next.second >= 0 && next.second < maps[0].size()
                && maps[next.first][next.second] == 1
                && visited[next.first][next.second] == 0
            ){
                dq.push_back(next);
                visited[next.first][next.second] = visited[curr.first][curr.second] + 1;
            }
        }
    }
    if (visited[maps.size()-1][maps[0].size()-1] == 0){
        return -1;
    }
    return visited[maps.size()-1][maps[0].size()-1];
}