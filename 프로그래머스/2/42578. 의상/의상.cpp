#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, vector<string>> clothes_map;
    
    for (int i = 0; i < clothes.size(); i ++){
        clothes_map[clothes[i][1]].push_back(clothes[i][0]);
    }
    for (auto it: clothes_map){
        answer  *= it.second.size() + 1;
    }
    
    return answer - 1;
}