#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    int xy_sum = (brown + 4) / 2;
    int xy_multiply = yellow - 4 + 2 * xy_sum;
    
    for (int i = 0; i < xy_sum; i++){
        if (i * (xy_sum - i) == xy_multiply){
            return {xy_sum - i, i};
        }
    }
}

// # x+y = (brown+4) / 2
// # xy = yellow - 4 + 2(x+y)