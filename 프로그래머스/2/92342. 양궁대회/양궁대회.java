import java.util.*;

class Solution {
    int maxScore = 0;
    int[] answer = new int[11];
    
    public int[] solution(int n, int[] info) {
        dfs(n, 0, new int[11], info);
        if (maxScore == 0) return new int[] {-1};
        return answer;
    }
    
    public void dfs(int n, int idx, int[] ryan, int[] info) {
        if (idx == 11) {
            update(n, ryan, info);                
            return;
        }
        
        // lose or draw
        if (idx == 10) {
            ryan[idx] = n;
            dfs(0, idx + 1, ryan, info);
            ryan[idx] = 0;
        } else {
            dfs(n, idx + 1, ryan, info);
        }
        
        // win
        if (n >= info[idx] + 1){
            ryan[idx] = info[idx] + 1;
            dfs(n - info[idx] - 1, idx + 1, ryan, info);
            ryan[idx] = 0;
        }
    }
    
    public void update(int n, int[] ryan, int[] info) {
        int score = 0;
        for (int i = 0; i < 11; i++) {
            if (ryan[i] > info[i]) score += 10 - i;
            else if (info[i] > 0) score -= 10 - i;
        }
        
        if (score > maxScore) {
            maxScore = score;
            answer = Arrays.copyOf(ryan, ryan.length);
        } else if (score == maxScore) {
            for (int i = 10; i >= 0; i--) {
                if (ryan[i] > answer[i]) {
                    answer = Arrays.copyOf(ryan, ryan.length);
                    break;
                } else if (answer[i] > ryan[i]) break;
            }
        }
    }
}