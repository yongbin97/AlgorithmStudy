#include <string>
#include <deque>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<string>> get_subvector(vector<string> ticket, vector<vector<string>> tickets){
    vector<vector<string>> subvector = tickets;
    subvector.erase(find(subvector.begin(), subvector.end(), ticket));
    return subvector;
}

vector<string> dfs(string airport, vector<vector<string>> tickets){
    vector<string> path;
    if (tickets.size() == 0){
        path.push_back(airport);
        return path;
    }
    
    vector<vector<string>> path_list;
    for (vector<string> ticket: tickets){
        if (ticket[0] == airport){
            vector<string> tmp_path = dfs(ticket[1], get_subvector(ticket, tickets));
            if (tmp_path.size() > 0){
                path_list.push_back(tmp_path);
            }
        }
    }
    if (path_list.size() > 0){
        sort(path_list.begin(), path_list.end());
        path = path_list.front();
        path.insert(path.begin(), airport);
    }
    return path;
}

vector<string> solution(vector<vector<string>> tickets) {
    return dfs("ICN", tickets);
}