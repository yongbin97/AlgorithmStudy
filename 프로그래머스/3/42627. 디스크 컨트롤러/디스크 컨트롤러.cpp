#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(vector<int> job1, vector<int> job2){
    if (job1[1] == job2[1]){
        return job1[0] < job2[0];
    }
    return job1[1] < job2[1];
}

vector<int> get_job(int time, vector<vector<int>> jobs){
    vector<vector<int>> job_list;
    for(vector<int> job: jobs){
        if (job[0] <= time){
            job_list.push_back(job);
        }
    }
    if (job_list.empty()){
        return vector<int>();
    }
    sort(job_list.begin(), job_list.end(), compare);
    return job_list.front();
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int size = jobs.size();
    
    int curr = 0;
    while (!jobs.empty()){
        vector<int> job = get_job(curr, jobs);
        if (job.empty()){
            curr++;
            continue;
        }
        curr += job[1];
        answer += curr - job[0];
        jobs.erase(find(jobs.begin(), jobs.end(), job));
    }
    return answer / size;
}