#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int p = 1;
    int q = 0;
    while ((n-q) / p > 0){
        if ((n-q) % p == 0){
            answer ++;
        }
        q += p;
        p ++;
    }
    
    return answer;
}