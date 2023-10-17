#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int ar[200];


int solution(vector<vector<int>> lines) {
    int answer = 0;
    
    for (int idx = 0; idx < lines.size(); idx ++){
        for (int i = lines[idx][0]; i < lines[idx][1]; i++){
            ar[i+100] ++;
        }
    }
    for (int i = 0; i < 200; i ++){
        if (ar[i] > 1){
            answer ++;
        }
    }
    
    return answer;
}