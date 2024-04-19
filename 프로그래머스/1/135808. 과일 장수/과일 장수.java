import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        Arrays.sort(score);
        for (int i = 0; i < score.length / m; i++){
            answer += score[score.length - i * m - m] * m;
        }
        
        return answer;
    }
}