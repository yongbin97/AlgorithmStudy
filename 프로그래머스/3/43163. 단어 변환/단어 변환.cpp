#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int answer = 100;

vector<string> get_next_words(string word, vector<string> words){
    vector<string> next_word_list;
    for (string w: words){
        int count = 0;
        for (int i = 0; i < word.size(); i++){
            if (word[i] != w[i]){
                count ++;
            }
        }
        if (count == 1){
            next_word_list.push_back(w);
        }
    }
    return next_word_list;
}

vector<string> get_subvector(string word, vector<string> words){
    words.erase(find(words.begin(), words.end(), word));
    return words;
}

void dfs(string curr, string target, vector<string> words, int count){
    if (curr == target){
        if (answer > count){
            answer = count;
        }
    }
    
    vector<string> next_word_list = get_next_words(curr, words);
    
    for (string next: next_word_list){
        dfs(next, target, get_subvector(next, words), count + 1);
    }
}

int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()){
        return 0;
    }
    dfs(begin, target, words, 0);
    return answer;
}