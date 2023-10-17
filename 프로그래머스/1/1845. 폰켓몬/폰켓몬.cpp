#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    unordered_map<int, int> map;
    for (int num: nums){
        map[num] += 1;
    }
    return min(map.size(), nums.size()/2);
}