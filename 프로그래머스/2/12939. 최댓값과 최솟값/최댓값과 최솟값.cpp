#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> split(string input, char delimiter){
    vector<int> answer;
    stringstream ss(input);
    string tmp;
    
    while (getline(ss, tmp, delimiter)){
        answer.push_back(stoi(tmp));
    }
    
    return answer;
}

string solution(string s) {
    vector<int> vc = split(s, ' ');
    sort(vc.begin(), vc.end());
    string answer = to_string(vc.front()) + " " + to_string(vc.back());
    return answer;
}