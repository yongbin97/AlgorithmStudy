#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end(), greater<>());
    for (int i = 0; i < citations.size(); i++){
        if (i+1 <= citations[i]){
            if (i + 1 > answer) answer = i+1;
        }
    }
    
    return answer;
}