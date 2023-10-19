#include <string>
#include <vector>
#include <iostream>

using namespace std;

// 0 1 1 2 3 5
int fibo(int n){
    int answ = 1;
    int prev = 0;
    int tmp = 0;
    for (int i = 1; i < n; i++){
        tmp = answ % 1234567;
        answ = (answ % 1234567 + prev % 1234567) % 1234567;
        prev = tmp;
    }
    return answ;
}

int solution(int n) {
    return fibo(n);
}