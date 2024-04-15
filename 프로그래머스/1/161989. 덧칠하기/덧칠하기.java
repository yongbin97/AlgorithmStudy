class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int curr = 0;
        
        for(int k : section){
            if (k > curr){
                curr = k + m - 1;
                answer ++;
            }
        }
        
        return answer;
    }
}