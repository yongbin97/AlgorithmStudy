import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (a, b) -> {
            if (a[1] == b[1]) return a[0] - b[0];
            else return a[1] - b[1];
        });
        
        int left = 0;
        for (int[] target: targets){
            if (left <= target[0]){
                answer += 1;
                left = target[1];
            }
        }
            
        return answer;
    }
}