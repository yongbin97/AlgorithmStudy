#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <functional>

using namespace std;

bool compare(const string &a, const string &b){
    if (b + a < a + b){
        return true;
    }
    return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> string_numbers;
    
    for (auto it: numbers){
        string_numbers.push_back(to_string(it));
    }
    sort(string_numbers.begin(), string_numbers.end(), compare);
    for (auto it: string_numbers) answer += it;
    if (answer[0] == '0'){
        return "0";
    }
    return answer;
}