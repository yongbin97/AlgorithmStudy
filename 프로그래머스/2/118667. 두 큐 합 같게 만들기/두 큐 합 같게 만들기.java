import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long total = 0;
        long sumOfQ1 = 0;
        
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for (int i = 0; i < queue1.length; i++) {
            q1.add(queue1[i]);
            q2.add(queue2[i]);
            
            total += queue1[i] + queue2[i];
            sumOfQ1 += queue1[i];
        }
        
        if (total % 2 == 1) return -1;

        while (true) {
            if (answer > queue1.length * 2 + 2) return -1;
            
            if (sumOfQ1 == total / 2) break;
            else if (sumOfQ1 > total / 2) {
                int move = q1.poll();
                
                q2.add(move);
                sumOfQ1 -= move;
            } else {
                int move = q2.poll();
                
                q1.add(move);
                sumOfQ1 += move;
            }
            answer++;
        }
        
        return answer;
    }
}