#include <string>
#include <vector>

using namespace std;
// 12 34 / 13 24/ 14 23

double getGradient(vector<int> dot1, vector<int> dot2){
    return double(dot1[1] - dot2[1])/double(dot1[0] - dot2[0]);
}

int solution(vector<vector<int>> dots) {
    int answer = 0;
    
    // {1, 2} {3, 4}
    if (getGradient(dots[0], dots[1]) == getGradient(dots[2], dots[3])){
        return 1;
    }
    else if (getGradient(dots[0], dots[2]) == getGradient(dots[1], dots[3])){
        return 1;
    }
    else if (getGradient(dots[0], dots[3]) == getGradient(dots[1], dots[2])){
        return 1;
    }
    
    
    return answer;
}