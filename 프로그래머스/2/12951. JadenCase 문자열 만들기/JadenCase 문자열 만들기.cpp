#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    
    answer += toupper(s[0]);
    
    for (int i = 1; i < s.size(); i++){
        s[i-1] == ' ' ? answer += toupper(s[i]): answer += tolower(s[i]); 
    }
    return answer;   
}