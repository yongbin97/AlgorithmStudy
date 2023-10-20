#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;


int answer = 0;
// d = 1 or -1  => sum += d * num
void dfs(vector<int> numbers, int target, int sum, int idx){
    if (idx == numbers.size()){
        if (sum == target){
            answer ++;
        }
        return;
    }
    
    dfs(numbers, target, sum + numbers[idx], idx+1);
    dfs(numbers, target, sum - numbers[idx], idx+1);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}