#include <string>
#include <iostream>
#include <cctype>

using namespace std;

bool solution(string s)
{
    int pCount = 0;
    int yCount = 0;
    for (int i = 0; i < s.size(); i++){
        if (tolower(s[i]) == 'p') pCount ++;
        else if (tolower(s[i]) == 'y') yCount ++;
    }
    return pCount == yCount;
}
