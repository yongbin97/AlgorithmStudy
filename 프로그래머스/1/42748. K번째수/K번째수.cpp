#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> sub_arr;
    
    for (int i = 0; i < commands.size(); i++){
        sub_arr = array;
        sort(sub_arr.begin() + commands[i][0] - 1, sub_arr.begin() + commands[i][1]);
        answer.push_back(sub_arr[commands[i][0] + commands[i][2] - 2]);
        cout << endl;
    }
    return answer;
}