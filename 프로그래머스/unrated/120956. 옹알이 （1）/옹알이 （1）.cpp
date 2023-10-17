#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    for (string bab: babbling){
        bool flag = true;
        for (int i = 0; i < bab.size(); i++){
            if (bab.substr(i, 3) == "aya") i+=2;
            else if (bab.substr(i, 2) == "ye") i += 1;
            else if (bab.substr(i, 3) == "woo") i += 2;
            else if (bab.substr(i, 2) == "ma") i += 1;
            else flag = false;
        }
        
        if (flag){
            answer ++;
        }
    }
    return answer;
}