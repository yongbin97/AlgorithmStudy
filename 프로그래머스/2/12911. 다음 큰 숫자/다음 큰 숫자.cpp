#include <string>
#include <vector>
#include <iostream>

using namespace std;
int get_count(int n){
    int count = 0;
    while (n>0){
        if (n % 2 != 0){
            count ++;
        }
        n = n / 2;
    }
    return count;
}

int solution(int n) {
    int answer = n + 1;
    int count = get_count(n);
    while (count != get_count(answer)){
        answer ++;
    }
    
    return answer;
}